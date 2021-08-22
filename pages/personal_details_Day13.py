from selenium.webdriver.common.by import By

from test_steps.base_methods import BaseMethods


class PersonalDetailsPageDay13(BaseMethods):
    HEADER = 'Personal Details'

    page_header = (By.CSS_SELECTOR, ".personalDetails h1")
    job = (By.XPATH, '//*[@id="sidenav"]//a[text()="Job"]')

    def get_page_header(self):
        return self.find_elem(self.page_header).text



