import pytest
from abc import ABC
from src.pages import MainPage


class BaseTest(ABC):
    """Класс конструктор `Test*`"""

    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver) -> None:
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
