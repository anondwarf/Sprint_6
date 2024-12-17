import allure
import random

from src.base import BasePage
from src.config import Links
from src.locators import OrderPageLocators as opl
from src.utils import GenerateTestData as gtd


class OrderPage(BasePage):
    """Страница оформления заказа"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = Links.ORDER_PAGE_URL

    @allure.step("Ввод имени")
    def enter_first_name(self) -> None:
        first_name = str(gtd.create_order_data().get("first_name"))
        self.enter_text(opl.INPUT_FIRST_NAME, first_name)

    @allure.step("Ввод фамилии")
    def enter_last_name(self) -> None:
        last_name = str(gtd.create_order_data().get("last_name"))
        self.enter_text(opl.INPUT_LAST_NAME, last_name)

    @allure.step("Ввод адреса")
    def enter_address(self) -> None:
        address = str(gtd.create_order_data().get("address"))
        self.enter_text(opl.INPUT_ADDRESS, address)

    @allure.step("Ввод номера телефона")
    def enter_phone(self) -> None:
        phone = str(gtd.create_order_data().get("phone_number"))
        self.enter_text(opl.INPUT_PHONE_NUMBER, phone)

    @allure.step("Ввод даты")
    def enter_date(self) -> None:
        date = str(gtd.create_order_data().get("date"))
        self.enter_text(opl.INPUT_DATE, date)
        self.click_keyboard_button_enter(opl.INPUT_DATE)

    @allure.step("Выбор станции метро")
    def choose_random_metro_station(self) -> None:
        self.click(opl.INPUT_METRO_STATION)
        metro_stations = self.find_all_elements(opl.LI_METRO_STATION_ITEM)
        metro_station = random.choice(metro_stations)
        metro_station.click()

    @allure.step("Клик по кнопке далее в форме 'Для кого самокат'")
    def click_next_button(self) -> None:
        self.click(opl.BUTTON_NEXT)

    @allure.step("Выбор срока аренды")
    def choose_random_rental_period(self) -> None:
        self.click(opl.INPUT_RENTAL_PERIOD)
        rental_periods = self.find_all_elements(opl.DIV_OPTION_RENTAL_PERIOD)
        rental_period = random.choice(rental_periods)
        rental_period.click()

    @allure.step("Выбор цвета самоката")
    def choose_random_scooter_color(self) -> None:
        elements = self.find_all_elements(opl.CHECKBOX_COLOR_SCOOTER)
        color = random.choice(elements)
        self.click(color)

    @allure.step("Клик по кнопке заказать в форме 'Про аренду'")
    def click_order_button(self) -> None:
        self.click(opl.BUTTON_ORDER)

    @allure.step("Проверка, что модальное окно было открыто")
    def is_modal_opened(self) -> bool:
        return self.is_element_present(opl.MODAL_HEADER)
