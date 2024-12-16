import time
import pytest

from src.base import BaseTest


class TestAccordion(BaseTest):
    """Тестирование выпадающего списка в разделе 'Вопросы о важном'"""

    def test_accordion_button_count(self) -> None:
        self.main_page.open()
        self.main_page.scroll_to_accordion()
        count_accordions = self.main_page.count_accordion_button()
        assert count_accordions == 8

    @pytest.mark.parametrize("index", range(8))
    def test_accordion_text(self, index: int) -> None:
        self.main_page.open()
        self.main_page.scroll_to_accordion()
        self.main_page.click_accoudion_button_by_index(index)
        actual_accordion = self.main_page.get_accordion_text_by_index(index)
        expected_accordion = self.get_test_data.get_accordion_text()
        assert actual_accordion == expected_accordion[index]
