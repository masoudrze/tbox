from selenium.webdriver.common.by import By

from pages.base_page import BasePage


USERNAME_INPUT = (By.ID, "username")


def test_base_page_can_type(driver):
    page = BasePage(driver)

    page.open()
    page.type(USERNAME_INPUT, "student")

    username = page.find(USERNAME_INPUT)

    assert username.get_attribute("value") == "student"
