import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_change_password_negative():
    driver.get("https://magento.softwaretestingboard.com/")
    sign_in_link = driver.find_element(By.LINK_TEXT, "Sign In")
    sign_in_link.click()

    email_field = driver.find_element(By.ID, 'email')
    email_field.send_keys("standard@user.user")

    password_field = driver.find_element(By.ID, 'pass')
    password_field.send_keys("Secret_sauce1")

    sign_in_btn = driver.find_element(By.ID, 'send2')
    sign_in_btn.click()
    time.sleep(3)

    greeting_text = driver.find_element(By.XPATH, '//header/div/div/ul/li/span').text
    assert greeting_text == 'Welcome, standard_user standard_user!'

    action_switch_btn = driver.find_element(By.XPATH, "//header//div/ul/li[2]/span/button")
    action_switch_btn.click()

    dropdown_account_link = driver.find_element(By.XPATH, '//header//div/ul/li/div/ul/li[1]/a')
    dropdown_account_link.click()

    edit_btn = driver.find_element(By.XPATH, '//main//div[1]/div[3]/div[2]/div[1]/div/a[1]')
    edit_btn.click()

    change_password_box = driver.find_element(By.ID, 'change-password')
    change_password_box.click()

    current_password_field = driver.find_element(By.ID, 'current-password')
    current_password_field.clear()
    current_password_field.send_keys("Secret_sauce1")

    save_btn = driver.find_element(By.XPATH, '//button [@title = "Save"]')
    save_btn.click()

    password_error_msg = driver.find_element(By.ID, 'password-error').text
    assert password_error_msg == 'This is a required field.'

    password_confirm_error_msg = driver.find_element(By.ID, 'password-confirmation-error').text
    assert password_confirm_error_msg == 'This is a required field.'

    driver.quit()



