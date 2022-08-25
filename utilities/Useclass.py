import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Useclass:

    def wait_test(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether all elements of given locator
            presence or not.If not then raise exception.The locator pass
            through from different page objects
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_all_elements_located(path))
        except Exception as e:
            self.log.info(f"{path} is not present to locate all elements")
            raise e

    def wait_clickable(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is clickable or not.If not then raise exception.The locator pass
            through from different page objects
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(path))
        except Exception as e:
            self.log.info(f"{path} is not clickable")
            raise e

    def verify_element(self, path):
        """
            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is present or not.If not then raise exception.
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(path))
        except Exception as e:
            self.log.info(f"{path} is not present to locate")
            raise e

    def window_handle(self):
        """
            Method used handle child window tab
        """
        return self.driver.switch_to.window(self.driver.window_handles[1])
