import pytest
from selenium import webdriver

from src.config import BrowsersOptions


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(options=BrowsersOptions.chrome_options())
    request.cls.driver = driver
    yield driver
    driver.quit()
