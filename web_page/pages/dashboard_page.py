from pages.base_page import BasePage
from config.settings import BASE_URL,ROUTES
from playwright.sync_api import Page

class DashboardPage(BasePage):
    LOGGED_IN_TEXT="a:has-text('Logged in as')"
    PRODUCT_LINK="a[href='/products']"
    CART_LINK="a[href='/view_cart']"
    LOGOUT_LINK="a[href='/logout']"

    def __init__(self,page:Page):
        super().__init__(page)

    def is_logged_in(self):
        self.page.wait_for_timeout(4000)
        return self.is_visible(self.LOGGED_IN_TEXT)

    def go_to_products(self):
        self.navigate(BASE_URL+ROUTES["products"])

    def go_to_cart(self):
        self.navigate(BASE_URL+ROUTES["cart"])

    def logout(self):
        self.click(self.LOGOUT_LINK)