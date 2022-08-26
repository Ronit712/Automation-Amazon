from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from utilities.Useclass import Useclass


class Homepage(Useclass):

    def __init__(self, driver):
        self.driver = driver

    search_text = (By.XPATH, '//div[@class="nav-search-field "]/input')
    list = (By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]/div/h2/a')
    button_buy = (By.XPATH, '//input[@id = "buy-now-button"]')

    def search_is_present(self, path):
        """
            Method used to return search path enable or not
        """
        try:
            self.driver.find_element(By.XPATH, path)
        except NoSuchElementException:
            return False
        return True

    def send_search_text(self, params):
        """
            Method used to search text
        """

        if self.search_is_present(Homepage.search_text[1]):
            self.driver.find_element(*Homepage.search_text).send_keys(params['product'])
            self.driver.find_element(*Homepage.search_text).send_keys(Keys.ENTER)

        else:
            self.log.info(f"{Homepage.search_text} is not present to locate")

    def list_is_present(self):
        """
            Method used to return product list present or not
        """
        list_present = False
        product_list = self.driver.find_elements(*Homepage.list)
        if len(product_list) >= 1:
            list_present = True
        return list_present

    def get_product_list(self):
        """
            Method used to get all product list of given search text
        """
        self.wait_test(Homepage.list)

        if self.list_is_present():
            return self.driver.find_elements(*Homepage.list)

    def scroll_down(self):
        """
            Method used to scroll down till the Buy now option for the selected product
        """
        self.window_handle()
        header = self.driver.find_element(*Homepage.button_buy)
        scrolling = self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
        return scrolling

    def click_buy(self):
        """
            Method used the Buy now option for the selected product
        """
        self.wait_clickable(Homepage.button_buy)
        return self.driver.find_element(*Homepage.button_buy).click()
