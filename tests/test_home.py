from pages.home_page import HomePage

def test_home_page_title(setup):
    assert "Automation Exercise" in setup.title


def test_navigate_to_login(setup):
    home = HomePage(setup)
    home.go_to_login()
    assert "login" in setup.current_url.lower()


def test_navigate_to_products(setup):
    home = HomePage(setup)
    home.go_to_products()
    assert "products" in setup.current_url.lower()


def test_navigate_to_cart(setup):
    home = HomePage(setup)
    home.go_to_cart()
    assert "view_cart" in setup.current_url.lower()


def test_home_page_loaded(setup):
    assert "automationexercise.com" in setup.current_url
