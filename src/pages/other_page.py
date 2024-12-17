from operator import contains
import time
from typing import Optional
from selenium.webdriver.support import expected_conditions as EC
from src.base import BasePage
from src.locators import BasePageLocator as bpl


class OtherPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url: Optional[str] = None

    def is_url_contains(self, _url: str) -> bool:
        new_url = self.driver.current_url
        check = contains(new_url, _url)
        return check
