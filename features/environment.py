from behave import *

# Possible other setup/ teardown functions you can create:
# before_all / after all
# before_feature / after_feature
# before_step / after_step

from selenium import webdriver

from test_steps.base_methods import BaseMethods
from tests import CHROME_PATH, DOMAIN


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(executable_path=CHROME_PATH)
    context.browser.get(DOMAIN)
    context.base_methods = BaseMethods(context.browser)


def after_scenario(context, scenario):
    context.browser.quit()
