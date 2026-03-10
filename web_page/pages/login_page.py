from pages.base_page import BasePage
from playwright.sync_api import Page
from config.settings import BASE_URL, ROUTES

class LoginPage(BasePage):
    EMAIL_INPUT    = "input[data-qa='login-email']"
    PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BUTTON   = "button[data-qa='login-button']"
    ERROR_MSG      = "p[style='color: red;']"
    LOGGED_IN_TEXT = "a:has-text('Logged in as')"
    SIGNUP_LOGIN = "a[href='/login']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate(BASE_URL)
        self.page.wait_for_timeout(2000)
        self.click("a[href='/login']")
        self.page.wait_for_timeout(2000)

    def login(self, email, password):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.page.wait_for_timeout(4000)     # ← wait for response!

    def is_logged_in(self) -> bool:
        self.page.wait_for_timeout(4000)     # ← wait!
        return self.is_visible(self.LOGGED_IN_TEXT)

    def is_on_login_page(self) -> bool:
        return self.is_visible(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        try:
            self.page.wait_for_selector(
                self.ERROR_MSG,
                state="visible",  # ← wait until visible!
                timeout=10000
            )
            return self.get_text(self.ERROR_MSG)
        except:
            return ""
