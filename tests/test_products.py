import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_view_product(setup):
    home = HomePage(setup)
    home.go_to_products()

    products = ProductsPage(setup)
    products.view_product_by_index(1)

    assert products.is_product_page_loaded()


def test_add_to_cart(setup):
    home = HomePage(setup)
    home.go_to_products()
    products = ProductsPage(setup)
    products.view_first_product()
    products.add_product_to_cart()
    products.continue_shopping()
    home.go_to_cart()
    cart = CartPage(setup)
    assert cart.is_product_in_cart()

def test_multiple_navigation(setup):
    home = HomePage(setup)
    home.go_to_products()
    home.go_to_cart()
    assert "Cart" in setup.page_source


def test_products_page_loads(setup):
    home = HomePage(setup)
    home.go_to_products()
    assert "products" in setup.current_url


def test_view_first_product_url(setup):
    home = HomePage(setup)
    home.go_to_products()
    products = ProductsPage(setup)
    products.view_first_product()
    assert "product_details" in setup.current_url


def test_view_second_product(setup):
    home = HomePage(setup)
    home.go_to_products()
    products = ProductsPage(setup)
    products.view_product_by_index(2)
    assert products.is_product_page_loaded()


def test_view_third_product(setup):
    home = HomePage(setup)
    home.go_to_products()
    products = ProductsPage(setup)
    products.view_product_by_index(3)
    assert products.is_product_page_loaded()


def test_view_product_by_index_zero_raises(setup):
    home = HomePage(setup)
    home.go_to_products()
    products = ProductsPage(setup)
    with pytest.raises(ValueError):
        products.view_product_by_index(0)


def test_view_product_by_index_negative_raises(setup):
    home = HomePage(setup)
    home.go_to_products()
    products = ProductsPage(setup)
    with pytest.raises(ValueError):
        products.view_product_by_index(-1)


def test_add_to_cart_continue_shopping_stays_on_product_page(setup):
    home = HomePage(setup)
    home.go_to_products()
    products = ProductsPage(setup)
    products.view_first_product()
    products.add_product_to_cart()
    products.continue_shopping()
    assert "product_details" in setup.current_url
