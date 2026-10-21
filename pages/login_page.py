from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT=(By.ID, "username")
    LOGIN_BUTTON = (By.XPATH, '//button[text()="ورود"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".login-alert.ng-binding")

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)


    def test_admin_can_login(driver, base_url):
        login_page = LoginPage(driver)

        driver.get(f"{base_url}")
        login_page.login("supervisor", "1")

        assert "/AdminIndex" in driver.current_url


def test_normal_user_can_login(driver, base_url):
    login_page = LoginPage(driver)

    driver.get(f"{base_url}")
    login_page.login("user2", "1")

    assert "/UserIndex" in driver.current_url
    assert "/AdminIndex" not in driver.current_url


def test_user_cannot_login_with_invalid_credentials(driver, base_url):
    login_page = LoginPage(driver)

    driver.get(f"{base_url}")
    login_page.login("invalid_username", "invalid_password")

    assert "/login" in driver.current_url
    assert login_page.get_error_message() == "Invalid username or password"

