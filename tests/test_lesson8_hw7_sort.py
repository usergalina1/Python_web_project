import math
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class TableSortTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)

        # wait = WebDriverWait(self.browser, 7)
        # wait.until(expected_conditions.url_contains("pim/viewEmployeeList"))

    def tearDown(self) -> None:
        self.browser.quit()

    # Part 2:
    # Using the site above create a test for sorting table values by First (Middle) Name column
    # 1. Login  (admin/password)
    # 2. Scroll down to the Employee list table
    # 3. Click the "First (Middle) Name" table header
    # 4. Wait for the sort to complete (hint: url)
    # 5. Ensure the records on the first page are listed in alphabetical order by name
    # Bonus Challenge:
    # Extend the test above to include all pages of employee records
    # Assume there can be more then the current number of pages and you don't know how many there will be eventually.
    def test_pim_table_first_name_sort(self):
        browser = self.browser
        wait = WebDriverWait(browser, 5)

        wait.until(expected_conditions.presence_of_element_located([By.LINK_TEXT, 'First (& Middle) Name'])).click()

        wait.until(expected_conditions.url_contains('sortOrder=ASC'))
        #or
        wait.until(expected_conditions.element_attribute_to_include(
            [By.LINK_TEXT, 'First (& Middle) Name'], 'class'
        ))

        list_of_first_elms = browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[3]')

        has_pagination = browser.find_elements(By.CLASS_NAME, 'desc')
        pages = 1
        if has_pagination:
            records = int(has_pagination[0].text.split()[-1])
            pages = math.ceil(records / 50)

        previous = ''
        for page in range(1, pages + 1):
            for name_elm in list_of_first_elms:
                current = name_elm.text
                self.assertGreaterEqual(current, previous,
                                        f"expected name '{current}' to be after '{previous}', but it was not")
                # print(f"Name '{current}' to be after '{previous}'")
                previous = current
            browser.find_element(By.LINK_TEXT, "Next").click()
            list_of_first_elms = browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[3]')









if __name__ == '__main__':
    unittest.main()
