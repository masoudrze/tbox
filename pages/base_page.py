from typing import TypeAlias

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import settings


Locator: TypeAlias = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            settings.default_timeout,
        )

    def open(self, url: str | None = None) -> None:
        self.driver.get(url or settings.base_url)

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_until_visible(self, locator: Locator) -> WebElement:
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator: Locator) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator: Locator, value: str) -> None:
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator: Locator) -> str:
        element = self.wait_until_visible(locator)
        return element.text
