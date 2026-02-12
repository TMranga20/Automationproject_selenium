def test_home_title(driver):
    driver.get("https://automationexercise.com")
    assert "automation" in driver.title.lower()


def test_navigation_links(driver):
    driver.get("https://automationexercise.com")
    assert "products" in driver.page_source.lower()


def test_footer_visible(driver):
    driver.get("https://automationexercise.com")
    assert "subscription" in driver.page_source.lower()
