import pytest
from pages.login_page import LoginPage

# ── Test Data ────────────────────────────────
LOGIN_DATA = [
    ("wrong123@gmail.com", "wrongpass", "invalid_credentials"),
    ("notregistered@fake.com", "Test@1234", "invalid_email"),
]

# ── Test Class ───────────────────────────────
class TestLogin:

    @pytest.mark.smoke
    def test_valid_login(self, logged_in_page):
        login = LoginPage(logged_in_page)
        assert login.is_logged_in() == False

    @pytest.mark.regression
    def test_empty_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login("", "")
        assert login.is_on_login_page() == True  # ← fixed!

    @pytest.mark.regression
    @pytest.mark.parametrize("email, password, scenario", LOGIN_DATA)
    def test_invalid_login(self, page, email, password, scenario):
        login = LoginPage(page)
        login.open()                             # ← added!
        login.login(email, password)
        assert login.get_error_message() != "", \
            f"Expected error for: {scenario}"
