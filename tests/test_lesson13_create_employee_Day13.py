import unittest
import time

from selenium.webdriver.common.by import By

from fixtures import AdminUserAuthentication

from menus.top_nav import TopNavMenu

from pages.add_employee import AddEmployeePage
from pages.add_employee_Day13 import AddEmployeePageDay13
from pages.employee_information import EmployeeInformationPage
from pages.job import JobPage
from pages.job_Day13 import JobPageDay13
from pages.personal_details import PersonalDetailsPage
from pages.personal_details_Day13 import PersonalDetailsPageDay13


class CreateEmployeeTest(AdminUserAuthentication):

    def setUp(self):
        super().setUp()

        self.top_menu = TopNavMenu(self.browser)

        self.personal_details_page_day13 = PersonalDetailsPageDay13(self.browser)
        self.job_page_day13 = JobPageDay13(self.browser)
        self.add_employee_page_day13 = AddEmployeePageDay13(self.browser)
        self.emp_info_page = EmployeeInformationPage(self.browser)

    def test_create_employee_no_creds(self):
        emp_id = str(int(time.time() * 1000))[4:]

        self.emp_info_page.click_add_btn()

        self.assertEqual(self.add_employee_page_day13.HEADER, self.add_employee_page_day13.get_page_header())
        self.add_employee_page_day13.enter_employee_details('Steve', 'Jones', emp_id)

        self.assertEqual(self.personal_details_page_day13.HEADER, self.personal_details_page_day13.get_page_header())
        #
        self.browser.find_element(By.XPATH, '//*[@id="sidenav"]//a[text()="Job"]').click()

        self.job_page_day13.update_job_info('HR')

        #
        self.browser.find_element(By.LINK_TEXT, "PIM").click()

        self.emp_info_page.search_for_employee_by_id(emp_id)
        rows = self.emp_info_page.get_all_employee_table_rows()
        self.assertEqual(1, len(rows))

        emp_info = self.emp_info_page.get_row_info(1)
        self.assertEqual('Steve', emp_info.get('first name'))
        self.assertEqual('Jones', emp_info.get('last name'))
        self.assertEqual('HR', emp_info.get('sub unit'))


