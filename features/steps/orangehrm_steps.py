import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def LaunchBrowser(context):

    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@then('verify logo is present on homepage')
def verifyLogo(context):
    time.sleep(10)
    status = context.driver.find_element(By.XPATH,
                                         '//body/div[@id="app"]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]').is_displayed()
    assert status is True


@then('close browser')
def step_impl(context):
    context.driver.close()
