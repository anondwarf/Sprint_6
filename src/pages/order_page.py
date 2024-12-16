from src.base import BasePage
from src.config import Links


class OrderPage(BasePage):
    """Страница оформления заказа"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = Links.ORDER_PAGE_URL
