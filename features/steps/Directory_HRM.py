from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('navigate to Admin tab')
def admin_Tab(context):
    time.sleep(10)
    context.driver.find_element(By.XPATH,
                                "//span[text()='Admin']").click()


@then('Enter user admin')
def enter_user_admin(context):
    timeout = 10
    # Wait until the 'Reset' button is clickable
    WebDriverWait(context.driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()=' Reset ']"))
    )

    # Locate the username field and enter text
    username_field = context.driver.find_element(By.XPATH, "//div[@class='']/input[@class='oxd-input oxd-input--active']")
    username_field.send_keys('vndjoelb96')


@then('Click Search and verify')
def Verify_Record(context):
    status = context.driver.find_element(By.XPATH,
                                         "//div[text()='vndjoelb96']").is_displayed()
    assert status is True
