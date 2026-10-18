import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


def get_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)

    if value is None:
        return default

    return value.strip().lower() in {"true", "1", "yes", "on"}


def get_int(name: str, default: int) -> int:
    value = os.getenv(name)

    if value is None:
        return default

    try:
        return int(value)
    except ValueError as error:
        raise ValueError(
            f"{name} must be an integer, but received: {value}"
        ) from error


@dataclass(frozen=True)
class Settings:
    base_url: str
    browser: str
    headless: bool
    default_timeout: int


def load_settings() -> Settings:
    base_url = os.getenv("BASE_URL", "").strip()
    browser = os.getenv("BROWSER", "chrome").strip().lower()
    headless = get_bool("HEADLESS", default=True)
    default_timeout = get_int("DEFAULT_TIMEOUT", default=10)

    if not base_url:
        raise ValueError("BASE_URL is required")

    if browser not in {"chrome", "firefox"}:
        raise ValueError(
            f"Unsupported browser: {browser}. "
            "Supported browsers are: chrome, firefox"
        )

    if default_timeout <= 0:
        raise ValueError("DEFAULT_TIMEOUT must be greater than zero")

    return Settings(
        base_url=base_url,
        browser=browser,
        headless=headless,
        default_timeout=default_timeout,
    )


settings = load_settings()
