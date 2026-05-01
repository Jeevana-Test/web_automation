from pages.base_page import BasePage
from playwright.sync_api import Page
from config.settings import BASE_URL,ROUTES

class ProductPage(BasePage):
    SEARCH_INPUT  = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    PAGE_TITLE    = "h2.title.text-center"
    PRODUCT_ITEMS = "div.col-sm-4"

 #category locators

    WOMEN_CATEGORY = "a[href='#Women']"
    DRESS_CATEGORY = "a[href='/category_products/1']"
    TOPS_CATEGORY = "a[href='/category_products/2']"
    SAREE_CATEGORY = "a[href='/category_products/7']"
    ADD_TO_CART = "a.add-to-cart"
    CONTINUE_SHOP = "button[data-dismiss='modal']"
    VIEW_CART = "u:has-text('View Cart')"

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

    def select_women_dress(self):
        self.click(self.WOMEN_CATEGORY)
        self.page.wait_for_timeout(1000)
        self.click(self.DRESS_CATEGORY)
        self.page.wait_for_timeout(1000)

    def click_women_category(self):
        self.click(self.WOMEN_CATEGORY)
        self.page.wait_for_timeout(1000)

    def click_dress_category(self):
        self.click(self.DRESS_CATEGORY)
        self.page.wait_for_timeout(1000)

    def add_first_product_to_cart(self):
        self.page.locator(self.ADD_TO_CART).first.click()
        self.page.wait_for_timeout(1000)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOP)
        self.page.wait_for_timeout(1000)

    def go_to_cart(self):
        self.click(self.VIEW_CART)
        self.page.wait_for_timeout(1000)