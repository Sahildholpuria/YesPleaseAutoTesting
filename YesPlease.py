from webdriver_manager.chrome import ChromeDriverManager
import time


def YesPlease(emailAddress, Password):

    websiteUrl = "https://www.yesplease.nl/home?lang=nl"
    coockieButton = "acceptAll-id"
    loginButon = "//header/nav[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/a[1]"
    emailField = "login-form-email"
    passwordField = "login-form-password"
    LoginButton = "//body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/button[1]"
    Home = "//header/nav[1]/div[3]/div[1]/div[1]/nav[1]/div[2]/ul[1]/div[1]/li[1]/a[1]"
    ProductCat = "//a[@id='Onze producten']"
    Product = "//body/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[4]/center[1]/div[1]/div[3]"
    AddToCart = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/button[1]"
    CheckOut = "//a[contains(text(),'AFREKENEN')]"

    # Check Out Details

    CheckOutName = "//input[@id='shippingFirstNamedefault']"
    CheckOutLastName = "//input[@id='shippingLastNamedefault']"
    CheckOutAddress = "//input[@id='shippingStreetdefault']"
    CheckOutHouseNumber = "//input[@id='shippingHouseNodefault']"
    CheckOutPin = "//input[@id='shippingZipCodedefault']"
    CheckOutResidence = "//input[@id='shippingCitydefault']"
    CheckOutPhone = "//input[@id='shippingPhoneNumberdefault']"
    CheckOutEmail = "//input[@id='emaildefault']"
    CheckOutCountry = "//select[@id='shippingCountrydefault']//option[@id='NL']"
    CheckOutProvidance = "//select[@id='shippingStatedefault']//option[@id='DR']"

    CardNumber = "//input[@id='rb_ideal']"
    ExpDate = "//input[@id='rb_ideal']"
    CVV = "//input[@id='rb_ideal']"


    from selenium import webdriver
    webdriver = webdriver.Chrome(ChromeDriverManager().install())
    webdriver.get(websiteUrl)
    time.sleep(1)
    webdriver.maximize_window()
    time.sleep(1)
    webdriver.find_element_by_id(coockieButton).click()
    time.sleep(1)
    webdriver.find_element_by_xpath(loginButon).click()
    time.sleep(1)
    webdriver.find_element_by_id(emailField).send_keys(emailAddress)
    time.sleep(1)
    webdriver.find_element_by_id(passwordField).send_keys(Password)
    time.sleep(1)
    # webdriver.find_element_by_name("loginRememberMe").get_attribute("checked")
    # time.sleep(1)
    webdriver.find_element_by_xpath(LoginButton).click()  # Login button
    time.sleep(1)
    webdriver.find_element_by_xpath(Home).click()
    time.sleep(1)
    webdriver.find_element_by_xpath(ProductCat).click()
    webdriver.execute_script("window.scrollTo(0,100)")
    for i in range(5):
        webdriver.find_element_by_xpath(Product).click()

    webdriver.find_element_by_xpath(AddToCart).click()
    time.sleep(3)
    webdriver.find_element_by_xpath(CheckOut).click()
    time.sleep(3)
    webdriver.find_element_by_xpath(CheckOutName).send_keys("Sahil")
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutLastName).send_keys("Kumar")
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutAddress).send_keys("Kamla Nagar")
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutHouseNumber).send_keys("1")
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutPin).send_keys("110012")
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutResidence).send_keys("Delhi")
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutPhone).send_keys("9876543210")
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutEmail).send_keys("")
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutCountry).click()
    time.sleep(1)
    webdriver.find_element_by_xpath(CheckOutProvidance).click()
    time.sleep(1)
    webdriver.find_element_by_xpath(CardNumber).send_keys("")
    time.sleep(1)
    webdriver.find_element_by_xpath(ExpDate).send_keys("")
    time.sleep(1)
    webdriver.find_element_by_xpath(CVV).send_keys("")
    time.sleep(1)
    webdriver.close()