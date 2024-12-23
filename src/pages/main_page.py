import allure

from src.base import BasePage
from src.config import Links
from src.locators import MainPageLocators as mpl


class MainPage(BasePage):
    """Главная страница"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = Links.MAIN_PAGE_URL

    @allure.step("Прокрутка страницы до блока 'Вопросы о важном'")
    def scroll_to_accordion(self) -> None:
        self.scroll_to(mpl.DIV_ACCORTION_HEADER)

    @allure.step("Подсчёт кол-ва вопросов в блоке 'Вопрсоы о важном'")
    def count_accordion_button(self) -> int:
        elements = self.find_all_elements(mpl.DIV_ACCORDION_BUTTON)
        return len(elements)

    @allure.step("Раскрытие ответа на вопрос в блоке 'Вопрсоы о важном'")
    def click_accoudion_button_by_index(self, index: int) -> None:
        elements = self.find_all_elements(mpl.DIV_ACCORDION_BUTTON)
        self.click(elements[index])

    @allure.step(
        "Получение текста ответа на вопрос в блоке 'Вопрсоы о важном'"
    )
    def get_accordion_text_by_index(self, index: int) -> str:
        elements = self.find_all_elements(mpl.P_ACCORDION)
        return elements[index].text

    @allure.step("Клик по кнопке 'Заказать' в блоке 'Как это работает'")
    def click_order_button_body(self) -> None:
        self.scroll_to(mpl.BUTTON_BODY_ORDER)
        self.click(mpl.BUTTON_BODY_ORDER)
