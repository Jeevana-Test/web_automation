import pytest
from pages.dashboard_page import DashboardPage

class TestDashboard:

    @pytest.mark.smoke

    def test_is_logged_in(self,logged_in_page):
        dashboard=DashboardPage(logged_in_page)
        assert dashboard.is_logged_in() == True

    @pytest.mark.regression
    def test_navigate_to_product(self,logged_in_page):
        dashboard=DashboardPage(logged_in_page)
        dashboard.go_to_products()
        assert "products" in logged_in_page.url

    @pytest.mark.regression

    def test_logout(self,logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        dashboard.logout()
        assert "login" in logged_in_page.url