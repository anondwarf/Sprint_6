from abc import ABC
from typing import Optional

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.locators import BasePageLocator as bpl


class BasePage(ABC):
    """Класс конструктор `*Page`"""

    def __init__(self, driver) -> None:
        self.driver = driver
        self.page_url: Optional[str] = None
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self) -> None:
        """Открывает страницу"""
        self.driver.get(self.page_url)

    def wait_load_page(self, url: str) -> bool:
        return self.wait.until(EC.url_contains(url))

    def is_opened(self) -> bool:
        """Проверяет, что страница открыта"""
        return self.wait.until(EC.url_to_be(str(self.page_url)))

    def is_opened_redirect(self, url: str) -> bool:
        return self.wait.until(EC.url_contains(url))

    def click(self, locator) -> None:
        """Клик по элементу"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find_all_elements(self, locator: tuple[str, str]):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
        return elements

    def scroll_to(self, locator: tuple[str, str]) -> None:
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_order_button_header(self) -> None:
        self.click(bpl.BUTTON_ORDER)

    def click_yandex_logo_header(self) -> None:
        self.click(bpl.LOGO_LINK_YANDEX)

    def click_scooter_logo_header(self) -> None:
        self.click(bpl.LOGO_LINK_SCOOTER)

    def enter_text(self, locator: tuple[str, str], text: str) -> None:
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(
            text
        )

    def is_element_present(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(locator))
        except:
            return False
        return True

    def click_keyboard_button_enter(self, locator: tuple[str, str]) -> None:
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(
            Keys.ENTER
        )

    def switch_tab(self):
        new_tab = self.driver.switch_to.window(self.driver.window_handles[-1])
        return new_tab
