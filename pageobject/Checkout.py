from selenium.webdriver.common.by import By

from utilities.Basepage import Basepage


class Checkout(Basepage):

    def __init__(self, driver):
        self.driver = driver

    email = (By.NAME, 'email')
    button_continue = (By.ID, 'continue')
    password = (By.XPATH, '//input[@type = "password"]')
    button_sign = (By.CSS_SELECTOR, 'input[id = "signInSubmit"]')
    alert = (By.XPATH, '//div[@class = "a-box-inner a-alert-container"]/div/ul/li/span')

    def send_email(self, params):
        """
            Method used to send mail for purchasing the product
        """
        return self.driver.find_element(*Checkout.email).send_keys(params['username'])

    def click_continue(self):
        """
            Method used to click continue button
        """
        self.wait_test(Checkout.button_continue)
        return self.driver.find_element(*Checkout.button_continue).click()

    def send_password(self, params):
        """
            Method used to send password
        """
        return self.driver.find_element(*Checkout.password).send_keys(params['password'])

    def click_sign_in(self):
        """
            Method used to click Sign in button
        """
        self.wait_clickable(Checkout.button_sign)
        return self.driver.find_element(*Checkout.button_sign).click()

    def verify_alert(self):
        """
            Method used to verify the alert text
        """
        self.verify_element(Checkout.alert)
        return self.driver.find_element(*Checkout.alert)
