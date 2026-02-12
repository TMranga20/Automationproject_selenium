import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage


@pytest.mark.regression
def test_regression_home_page_load(setup):
    assert "Automation Exercise" in setup.title


@pytest.mark.regression
def test_regression_navigation_to_products(setup):
    home = HomePage(setup)
    home.go_to_products()
    assert "All Products" in setup.page_source


@pytest.mark.regression
def test_regression_navigation_to_login(setup):
    home = HomePage(setup)
    home.go_to_login()
    assert "Login" in setup.page_source


@pytest.mark.regression
def test_regression_add_single_product_to_cart(setup):
    home = HomePage(setup)
    home.go_to_products()

    products = ProductsPage(setup)
    products.view_first_product()
    products.add_product_to_cart()
    products.continue_shopping()

    home.go_to_cart()
    cart = CartPage(setup)

    assert cart.is_product_in_cart()


@pytest.mark.regression
def test_regression_add_product_and_validate_url(setup):
    home = HomePage(setup)
    home.go_to_products()

    products = ProductsPage(setup)
    products.view_first_product()

    assert "product_details" in setup.current_url


@pytest.mark.regression
def test_regression_multiple_navigation_flow(setup):
    home = HomePage(setup)

    home.go_to_products()
    home.go_to_cart()
    home.go_to_login()

    assert "Login" in setup.page_source


@pytest.mark.regression
def test_regression_browser_back_forward(setup):
    home = HomePage(setup)

    home.go_to_products()
    setup.back()
    setup.forward()

    assert "Products" in setup.page_source


@pytest.mark.regression
def test_regression_invalid_login_flow(setup):
    home = HomePage(setup)
    home.go_to_login()

    login = LoginPage(setup)
    login.login("wrong@email.com", "wrongpassword")

    assert "incorrect" in login.get_error_message()


@pytest.mark.regression
def test_regression_empty_cart_validation(setup):
    home = HomePage(setup)
    home.go_to_cart()

    assert "Cart is empty" in setup.page_source or "Shopping Cart" in setup.page_source


@pytest.mark.regression
def test_regression_refresh_and_validate_title(setup):
    setup.refresh()
    assert "Automation Exercise" in setup.title
