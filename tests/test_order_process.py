import time
from src.base import BaseTest


class TestOrderProcess(BaseTest):
    """Тестирование процесса заказа самоката"""

    def test_header_order_button(self) -> None:
        self.main_page.open()
        self.main_page.click_order_button_header()
        assert self.order_page.is_opened() == True

    def test_boody_order_button(self) -> None:
        self.main_page.open()
        self.main_page.click_order_button_body()
        assert self.order_page.is_opened() == True

    def test_order_form(self) -> None:
        self.main_page.open()
        self.main_page.click_order_button_header()
        self.order_page.enter_first_name()
        self.order_page.enter_last_name()
        self.order_page.enter_address()
        self.order_page.choose_random_metro_station()
        self.order_page.enter_phone()
        self.order_page.click_next_button()
        self.order_page.enter_date()
        self.order_page.choose_random_rental_period()
        self.order_page.choose_random_scooter_color()
        self.order_page.click_order_button()
        assert self.order_page.is_modal_opened() == True
