from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

from core.config import settings


def create_driver() -> WebDriver:
    if settings.browser == "chrome":
        return create_chrome_driver()

    if settings.browser == "firefox":
        return create_firefox_driver()

    raise ValueError(f"Unsupported browser: {settings.browser}")


def create_chrome_driver() -> WebDriver:
    options = ChromeOptions()

    if settings.headless:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")

    return webdriver.Chrome(options=options)


def create_firefox_driver() -> WebDriver:
    options = FirefoxOptions()

    if settings.headless:
        options.add_argument("-headless")

    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)

    return driver
