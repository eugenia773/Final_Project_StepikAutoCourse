from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_addToBasket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_addToBasket.click()
        