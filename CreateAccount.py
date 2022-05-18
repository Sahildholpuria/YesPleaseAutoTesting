import pytest
from webdriver_manager.chrome import ChromeDriverManager
import time

def CreateAccount(FirstName, LastName, PhoneNumber, Email, Password):
    from selenium import webdriver
    webdriver = webdriver.Chrome(ChromeDriverManager().install())
    print("===============YesPlease Create Account===============")
    webdriver.get("https://www.yesplease.nl/home?lang=nl")
    time.sleep(1)
    webdriver.find_element_by_id("acceptAll-id").click()
    time.sleep(1)
    webdriver.find_element_by_xpath(
        "//header/nav[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/a[1]").click()
    time.sleep(1)
    webdriver.find_element_by_xpath(
        "//a[@id='register-tab']").click()  # Create an Account
    time.sleep(1)
    webdriver.execute_script("window.scroll(0,200)")
    webdriver.find_element_by_xpath(
        "//body[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[1]/div[1]/div[1]/input[1]").send_keys(FirstName)  # First Name
    webdriver.find_element_by_xpath(
        "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[1]/div[2]/div[1]/input[1]").send_keys(LastName)  # Last Name
    webdriver.find_element_by_xpath(
        "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[1]/div[3]/div[1]/input[1]").send_keys(PhoneNumber)  # Phone Number
    webdriver.find_element_by_xpath(
        "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[2]/div[1]/div[1]/input[1]").send_keys(Email)  # Email
    webdriver.find_element_by_xpath(
        "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[2]/div[2]/div[1]/input[1]").send_keys(Email)  # Confirm Email
    webdriver.find_element_by_xpath(
        "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[3]/div[1]/div[1]/input[1]").send_keys(Password)  # Password
    webdriver.find_element_by_xpath(
        "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[3]/div[2]/div[1]/input[1]").send_keys(Password)  # Confirm Password
    time.sleep(2)
    webdriver.find_element_by_xpath(
        "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[2]/div[4]/div[1]/button[1]").click()
    time.sleep(5)
    