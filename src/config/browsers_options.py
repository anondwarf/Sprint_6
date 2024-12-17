from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowsersOptions:
    """Настройки запуска браузеров"""

    @staticmethod
    def chrome_options() -> Options:
        """Настройки запуска браузера Chrome"""
        opt = webdriver.ChromeOptions()
        # opt.add_argument("--blink-settings=imagesEnabled=false")
        # opt.add_argument("--headless")
        opt.add_argument("--log-level=1")
        return opt
