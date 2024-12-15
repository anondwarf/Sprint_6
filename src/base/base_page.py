from abc import ABC
from typing import Optional
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(ABC):
    """Класс конструктор `*Page`"""

    def __init__(self, driver) -> None:
        self.driver = driver
        self.page_url: Optional[str] = None
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self) -> None:
        """Открывает страницу"""
        self.driver.get(self.page_url)

    def is_opened(self) -> bool:
        """Проверяет, что страница открыта"""
        return self.wait.until(EC.url_to_be(str(self.page_url)))

    def click(self, locator: tuple[str, str]) -> None:
        """Клик по элементу"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
