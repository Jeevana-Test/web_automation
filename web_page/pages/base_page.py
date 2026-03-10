from playwright.sync_api import Page
from config.settings import TIMEOUT

class BasePage:
    def __init__(self, page: Page):
        self.page    = page
        self.timeout = TIMEOUT

    def navigate(self, url):
        self.page.goto(url, timeout=60000)  # ← 60 seconds!
        self.page.wait_for_load_state("domcontentloaded")

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)  # ← no clear()!

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()