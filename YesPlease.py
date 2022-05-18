from webdriver_manager.chrome import ChromeDriverManager
import time


def YesPlease(emailAddress, Password):
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
    time.sleep(1)
    webdriver.find_element_by_xpath(
        "//header/nav[1]/div[3]/div[1]/div[1]/nav[1]/div[2]/ul[1]/div[1]/li[1]/a[1]").click()
    time.sleep(1)
    webdriver.find_element_by_xpath("//a[@id='Onze producten']").click()
    webdriver.execute_script("window.scrollTo(0,100)")
    for i in range(10):
        webdriver.find_element_by_xpath(
            "//body/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[4]/center[1]/div[1]/div[3]").click()

    webdriver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/button[1]").click()
    time.sleep(5)
    webdriver.find_element_by_xpath("//a[contains(text(),'AFREKENEN')]").click()
    time.sleep(5)
