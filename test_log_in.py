import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

text_box_username_name= "username"
text_box_pass_name= "password"
btn_Log_in_xpath= "//button[@type='submit']"
sign_in_url= "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def test_log_in_verification_with_valid_data(browser):
    driver=browser
    driver.get(sign_in_url)
    time.sleep(2)
    driver.find_element(By.NAME,text_box_username_name).send_keys("Admin")
    time.sleep(2)
    driver.find_element(By.NAME,text_box_pass_name ).send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH,btn_Log_in_xpath).click()
    time.sleep(2)

    expected_title = "OrangeHRM"  # adjust to the real title (e.g., "OrangeHRM" or "Dashboard - OrangeHRM")
    actual_title = driver.title
    print("title",actual_title)
    assert actual_title == expected_title, "Title mismatched"



