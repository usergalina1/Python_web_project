import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By


from steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


# Part 1:
# Create at least 3 negative tests for the login functionality of the following site:
# http://hrm-online.portnov.com
# example: blank username

class NegativeLoginTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_empty_credentials(self):
        self.browser.find_element(By.ID, "btnLogin").click()
        self.assertEqual('Username cannot be empty', self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]').text)

    def test_empty_login(self):
        self.browser.find_element(By.ID, "txtPassword").send_keys("password")
        self.browser.find_element(By.ID, "btnLogin").click()
        self.assertEqual('Username cannot be empty', self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]').text)

    def test_empty_password(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys("admin")
        self.browser.find_element(By.ID, "btnLogin").click()
        self.assertEqual('Password cannot be empty', self.browser.find_element(By.ID, 'spanMessage').text)

    def test_invalid_credentials(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys("12345")
        self.browser.find_element(By.ID, "txtPassword").send_keys("122345")
        self.browser.find_element(By.ID, "btnLogin").click()
        self.assertEqual('Invalid credentials', self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]').text)

    # or I can ccreate parameterized TC

    @parameterized.expand([
        ('empty credentials', '', '', 'Username cannot be empty'),
        ('empty username', '', 'password', 'Username cannot be empty'),
        ('empty password', 'admin', '', 'Password cannot be empty'),
        ('invalid credentials', '12345', '12345', 'Invalid credentials')
    ])
    def test_invalid_login_credentials(self, test_name, username, password, expected_result):
        authenticate(self.browser, username=username, password=password)
        self.assertEqual(expected_result, self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]').text)


if __name__ == '__main__':
    unittest.main()
