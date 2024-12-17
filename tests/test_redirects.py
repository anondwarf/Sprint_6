import pytest
from src.base import BaseTest


class TestRedirects(BaseTest):
    """Тестирование редиректов"""

    def test_redirect_to_main_page_from_header_link(self) -> None:
        self.order_page.open()
        self.order_page.click_scooter_logo_header()
        assert self.main_page.is_opened() == True

    @pytest.mark.parametrize("_url", ["https://dzen.ru/"])
    def test_redirect_to_dzen_page(self, _url) -> None:
        self.main_page.open()
        self.main_page.click_yandex_logo_header()
        self.other_page.switch_tab()
        self.other_page.wait_load_page(_url)
        assert self.other_page.is_url_contains(_url) == True
