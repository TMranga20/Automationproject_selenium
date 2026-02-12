import os
import pytest
from utils.driver_setup import get_driver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get("https://automationexercise.com")

    # Handle Google vignette/ad redirects that intermittently appear.
    if "google_vignette" in driver.current_url:
        driver.get("https://automationexercise.com")
    WebDriverWait(driver, 30).until(lambda d: "Automation Exercise" in d.title)

    yield driver
    driver.quit()


@pytest.fixture
def driver(setup):
    return setup


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    test_driver = item.funcargs.get("setup") or item.funcargs.get("driver")
    if not test_driver:
        return

    try:
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/{item.name}.png"
        test_driver.save_screenshot(screenshot_path)
    except WebDriverException:
        # Avoid masking the real test failure when the browser/window is already gone.
        pass
