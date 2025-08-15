import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():

   driver=webdriver.Chrome()

   driver.maximize_window()

   print("\nBrowser launched and maximized.")

   yield driver

   print("\nQuitting browser.")

   driver.quit()