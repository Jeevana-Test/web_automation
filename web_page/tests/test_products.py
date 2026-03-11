import pytest
from pages.product_page import ProductPage

class TestProducts:

    @pytest.mark.smoke
    def test_product_page_loads(self, logged_in_page):
        product = ProductPage(logged_in_page)
        product.open()
        assert product.is_product_page() == True

    @pytest.mark.regression
    def test_search_products(self, logged_in_page):
        product = ProductPage(logged_in_page)
        product.open()
        product.search_product("women")
        assert product.product_count() > 0

    @pytest.mark.regression
    def test_product_count(self, logged_in_page):
        product = ProductPage(logged_in_page)
        product.open()
        count = product.product_count()
        assert count > 0

