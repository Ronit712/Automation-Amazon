from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.Baseclass import Baseclass
from utilities.Useclass import Useclass


class Homepage(Baseclass, Useclass):

    def __init__(self, driver):
        self.driver = driver

    search_text = (By.XPATH, '//div[@class="nav-search-field "]/input')
    list = (By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]/div/h2/a')
    button_buy = (By.XPATH, '//input[@id = "buy-now-button"]')

    def send_search_text(self, params):
        """
            Method used to search text
        """

        if self.search_is_present(Homepage.search_text[1]):
            self.driver.find_element(*Homepage.search_text).send_keys(params['product'])
            self.driver.find_element(*Homepage.search_text).send_keys(Keys.ENTER)

    def get_product_list(self):
        """
            Method used to get all product list of given search text
        """
        log = self.get_logger()
        self.wait_test(Homepage.list)

        if self.list_is_present(Homepage.list[1]):
            return self.driver.find_elements(*Homepage.list)
        else:
            log.info(f"The path {Homepage.list} not present")

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
        if self.search_is_present(Homepage.button_buy[1]):
            self.driver.find_element(*Homepage.button_buy).click()
