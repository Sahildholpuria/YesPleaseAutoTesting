from webdriver_manager.chrome import ChromeDriverManager
import time


def YesPlease(emailAddress,Password):
    from selenium import webdriver
    webdriver = webdriver.Chrome(ChromeDriverManager().install())
    webdriver.get("https://www.yesplease.nl/home?lang=nl")
    time.sleep(1)
    webdriver.maximize_window()
    time.sleep(1)
    webdriver.find_element_by_id("acceptAll-id").click()
    time.sleep(1)
    webdriver.find_element_by_xpath(
        "//header/nav[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/a[1]").click()
    time.sleep(1)
    webdriver.find_element_by_id(
        "login-form-email").send_keys(emailAddress)
    time.sleep(1)
    webdriver.find_element_by_id("login-form-password").send_keys(Password)
    time.sleep(1)
    # webdriver.find_element_by_name("loginRememberMe").get_attribute("checked")
    # time.sleep(1)
    webdriver.find_element_by_xpath(
        "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/button[1]").click()  # Login button
    time.sleep(10)
    # webdriver.find_element_by_xpath(
    #     "//header/nav[1]/div[3]/div[1]/div[1]/nav[1]/div[2]/ul[1]/div[1]/li[1]/a[1]").click()  # Home Page
    # time.sleep(1)
    # webdriver.find_element_by_xpath(
    #     "/html[1]/body[1]/div[1]/header[1]/nav[1]/div[3]/div[1]/div[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]").click()  # Product Page
    # time.sleep(1)
    # webdriver.find_element_by_xpath(
    #     "//body/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[4]/center[1]/div[1]/div[3]/i[1]").click()  # Add to cart
    # time.sleep(1)
    # webdriver.find_element_by_xpath(
    #     "//body/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/button[1]").click()  # Proceed to checkout
    # time.sleep(1)
    # webdriver.find_element_by_xpath(
    #     "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/a[1]").click()  # Checkout
    # time.sleep(1)
    # webdriver.find_element_by_xpath(
    #     "//input[@id='shippingFirstNamedefault']").clear()
    # webdriver.find_element_by_xpath(
    #     "//input[@id='shippingLastNamedefault']").clear()
    # webdriver.find_element_by_xpath(
    #     "//input[@id='shippingFirstNamedefault']").send_keys("Sahil")
    # webdriver.find_element_by_xpath(
    #     "//input[@id='shippingLastNamedefault']").send_keys("Dholpuria")
    # time.sleep(10)
