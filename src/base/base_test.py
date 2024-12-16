from abc import ABC

import pytest

from src.pages import MainPage
from src.utils import GetTestData, GenerateTestData


class BaseTest(ABC):
    """Класс конструктор `Test*`"""

    main_page: MainPage
    get_test_data: GetTestData
    generate_test_data: GenerateTestData

    @pytest.fixture(autouse=True)
    def setup(self, request, driver) -> None:
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.get_test_data = GetTestData()
        request.cls.generate_test_data = GenerateTestData()
