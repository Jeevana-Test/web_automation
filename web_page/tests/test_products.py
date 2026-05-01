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

    @pytest.mark.regression

    def test_women_dress_category(self,logged_in_page):
        product=ProductPage(logged_in_page)
        product.open()
        product.select_women_dress()
        assert "category_products" in logged_in_page.url
        assert product.product_count() > 0

    @pytest.mark.regression
    def test_add_dress_to_cart(self, logged_in_page):
        products = ProductPage(logged_in_page)
        products.open()
        products.click_women_category()
        products.click_dress_category()
        products.add_first_product_to_cart()  # add 1st!
        products.continue_shopping()  # dismiss popup!
        products.add_first_product_to_cart()  # add 2nd!
        products.go_to_cart()  # go to cart!
        # verify cart has items
        assert "view_cart" in logged_in_page.url

