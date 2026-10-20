from urllib.parse import urlparse

from core.config import settings


def test_driver_opens_base_url(driver):
    driver.get(settings.base_url)

    expected_domain = urlparse(settings.base_url).netloc
    actual_domain = urlparse(driver.current_url).netloc

    assert actual_domain == expected_domain
