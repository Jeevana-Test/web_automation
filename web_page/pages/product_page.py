from pages.base_page import BasePage
from playwright.sync_api import Page
from config.settings import BASE_URL,ROUTES

class ProductPage(BasePage):
    SEARCH_INPUT  = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    PAGE_TITLE    = "h2.title.text-center"
    PRODUCT_ITEMS = "div.col-sm-4"

    def __init__(self,page:Page):
        super().__init__(page)

    def open(self):
        self.navigate(BASE_URL+ROUTES["products"])

    def search_product(self,product_name):
        self.fill(self.SEARCH_INPUT,product_name)
        self.click(self.SEARCH_BUTTON)

    def is_product_page(self):
        return self.is_visible(self.PAGE_TITLE)

    def product_count(self):
        return self.page.locator(self.PRODUCT_ITEMS).count()

