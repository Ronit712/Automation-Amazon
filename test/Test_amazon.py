from Testdata.testdata import Testdata
from pageobject.Checkout import Checkout
from utilities.Baseclass import Baseclass
from pageobject.Homepage import Homepage


class Test(Baseclass):
    """
    Test case for amazon to validate title,give product,select product,click buy now option,give username,
    password and validate the alert text
    """

    def test_amazon(self, params):
        self.driver.implicitly_wait(10)
        log = self.get_logger()
        title = self.driver.title
        try:
            assert (Testdata.verify_title in title)

        except Exception as e:
            raise e
        log.info("Title is" + title)
        '''initialize the Homepage object model and give user product'''
        home = Homepage(self.driver)
        home.send_search_text(params)
        log.info("searching completed successfully")
        products = home.get_product_list()
        i = 0
        no_of_products = (len(products))
        log.info(f"Total no of products getting {no_of_products}")
        '''Select the fourth item '''
        for product in products:
            log.info("List of products are" + product.text)
            i = i + 1
            if i == 4:
                product.click()
        log.info("Select fourth product successfully")
        home.scroll_down()
        home.click_buy()
        log.info("Successfully Buy now the product ")
        checkout = Checkout(self.driver)
        '''Send user email,password '''
        checkout.send_email(params)
        checkout.click_continue()
        log.info("send username")
        checkout.send_password(params)
        checkout.click_sign_in()
        log.info("send password")
        try:
            alert = checkout.verify_alert().text
            if Testdata.text_alert in alert:
                assert (Testdata.text_alert in alert)
            else:
                assert (Testdata.text_alert_second in alert)
        except Exception as e:
            raise e

        log.info(f"alert text is {alert}")
        log.info("verify the text successfully ")


