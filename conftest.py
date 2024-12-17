import pytest
from selenium import webdriver

from src.config import BrowsersOptions


@pytest.fixture(autouse=True)
def driver(request):
    """
    Автоматически устанавливает драйвер браузера для каждого теста.

    :param request: Запрос, который содержит информацию о тесте
    """
    driver = webdriver.Chrome(options=BrowsersOptions.chrome_options())
    request.cls.driver = driver
    yield driver
    driver.quit()
