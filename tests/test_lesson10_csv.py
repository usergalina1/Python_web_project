import os
import csv
import unittest
from typing import List

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_steps.common import authenticate
from tests import CHROME_PATH, DOMAIN, PROJ_HOME


def read_csv(header=True) -> List:
    with open(os.path.join(PROJ_HOME, 'data', 'login_data.csv')) as file:
        reader = csv.reader(file)
        if header:
            next(reader)  # only needed if CSV has headers, otherwise it should be skipped
        return list(map(tuple, reader))


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    # @parameterized.expand([
    #     ('invalid password', 'admin', '123abc', 'Invalid credentials'),
    #     ('empty username', '', '123abc', 'Username cannot be empty'),
    #     ('empty password', 'admin', '', 'Password cannot be empty')
    # ])
    @parameterized.expand(read_csv)
    def test_invalid_credentials(self, test_name, username, password, expected_error_message):
        authenticate(self.browser, username=username, password=password)
        message = self.browser.find_elements(By.ID, 'spanMessage')
        self.assertTrue(message)
        self.assertEqual(expected_error_message, message[0].text)


if __name__ == '__main__':
    unittest.main()
