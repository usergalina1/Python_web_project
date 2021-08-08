from selenium.webdriver.common.by import By

from tests import ADMIN_USER, DEFAULT_PASSWORD


def authenticate(browser, username=ADMIN_USER, password=DEFAULT_PASSWORD):
    #example of documentation
    """
    used to login into  Orange HRM
    :param browser:
    :return: None
    """
    #regular comments
    #TODO: need to add param
    browser.find_element(By.ID, "txtUsername").send_keys(username)
    browser.find_element(By.ID, "txtPassword").send_keys(password)
    browser.find_element(By.ID, "btnLogin").click()