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
