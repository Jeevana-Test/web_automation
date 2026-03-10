import pytest
from playwright.sync_api import sync_playwright
from config.settings import HEADLESS, USERS
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()

    # block all ads!
    context.route("**/*googlesyndication*", lambda route: route.abort())
    context.route("**/*doubleclick*",       lambda route: route.abort())
    context.route("**/*googleadservices*",  lambda route: route.abort())
    context.route("**/*adsbygoogle*",       lambda route: route.abort())

    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def logged_in_page(page):
    login = LoginPage(page)
    login.open()
    login.login(
        USERS["valid_user"]["email"],
        USERS["valid_user"]["password"]
    )
    page.wait_for_selector(
        "a:has-text('Logged in as')",
        timeout=15000
    )
    print(f"\nURL after login: {page.url}")
    print(f"Logged in: {login.is_logged_in()}")
    yield page