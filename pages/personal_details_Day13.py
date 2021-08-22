from selenium.webdriver.common.by import By

from pages.add_employee_Day13 import BasePage
from test_steps.base_methods import BaseMethods


class PersonalDetailsPageDay13(BasePage):
    HEADER = 'Personal Details'
    PAGE_URL = '/pim/viewPersonalDetails/empNumber/'

    page_header = (By.CSS_SELECTOR, ".personalDetails h1")





