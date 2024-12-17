from abc import ABC

import pytest

from src.pages import MainPage, OrderPage, OtherPage
from src.utils import GenerateTestData, GetTestData


class BaseTest(ABC):
    """Класс конструктор `Test*`"""

    main_page: MainPage
    order_page: OrderPage
    other_page: OtherPage
    get_test_data: GetTestData
    generate_test_data: GenerateTestData

    @pytest.fixture(autouse=True)
    def setup(self, request, driver) -> None:
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.order_page = OrderPage(driver)
        request.cls.other_page = OtherPage(driver)
        request.cls.get_test_data = GetTestData()
        request.cls.generate_test_data = GenerateTestData()
