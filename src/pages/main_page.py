from src.base import BasePage
from src.config import Links


class MainPage(BasePage):
    """Главная страница"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = Links.MAIN_PAGE_URL
