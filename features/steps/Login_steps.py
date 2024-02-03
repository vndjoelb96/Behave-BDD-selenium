import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I launch the chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open the OrangeHRM homepage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@when('Enter username {user} and password {pwd}')
def step_impl(context, user, pwd):
    time.sleep(5)
    username_input = context.driver.find_element(By.NAME, 'username')
    password_input = context.driver.find_element(By.NAME, 'password')

    # Clear existing text in the fields (optional, depending on your scenario)
    username_input.clear()
    password_input.clear()

    # Enter username and password
    username_input.send_keys(user)
    password_input.send_keys(pwd)


@when('Click login button')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, '//button[@type="submit"]').click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    # Define the XPath
    dash = '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]'
    try:
        # Use WebDriverWait to wait for the element to be present and contain text
        element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, dash)))
        text = element.text
    except:
        context.driver.close()
        assert False, 'test failed'
    if text == "Dashboard":
        assert True, 'test is passed'
        context.driver.close()

    # Close the WebDriver after each scenario

