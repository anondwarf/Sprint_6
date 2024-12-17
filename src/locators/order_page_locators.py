class OrderPageLocators:
    """Локаторы `OrderPage`"""

    INPUT_FIRST_NAME: tuple[str, str] = (
        "xpath",
        "//input[@placeholder='* Имя']",
    )
    INPUT_LAST_NAME: tuple[str, str] = (
        "xpath",
        "//input[@placeholder='* Фамилия']",
    )
    INPUT_ADDRESS: tuple[str, str] = (
        "xpath",
        "//input[@placeholder='* Адрес: куда привезти заказ']",
    )
    INPUT_METRO_STATION: tuple[str, str] = (
        "xpath",
        "//input[@placeholder='* Станция метро']",
    )
    INPUT_PHONE_NUMBER: tuple[str, str] = (
        "xpath",
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    )
    BUTTON_NEXT: tuple[str, str] = (
        "xpath",
        "//button[contains(text(), 'Далее')]",
    )
    INPUT_DATE: tuple[str, str] = (
        "xpath",
        "//input[@placeholder='* Когда привезти самокат']",
    )
    INPUT_RENTAL_PERIOD: tuple[str, str] = (
        "xpath",
        "//div[@class='Dropdown-control']",
    )
    DIV_OPTION_RENTAL_PERIOD: tuple[str, str] = (
        "xpath",
        "//div[@class='Dropdown-option']",
    )
    CHECKBOX_COLOR_SCOOTER: tuple[str, str] = (
        "xpath",
        "//input[@type='checkbox']",
    )
    BUTTON_ORDER: tuple[str, str] = (
        "xpath",
        "//button[contains(@class, 'Middle') and contains(text(), 'Заказать')]",
    )
    MODAL_HEADER: tuple[str, str] = (
        "xpath",
        "//div[contains(@class, 'Order_ModalHeader')]",
    )
    BUTTON_APPROVE_ORDER: tuple[str, str] = ("xpath", "//button[text()='Да']")
    BUTTON_DETAILS_ORDER: tuple[str, str] = (
        "xpath",
        "//button[text()='Посмотреть статус']",
    )
    LI_METRO_STATION_ITEM: tuple[str, str] = (
        "xpath",
        "//li[@role='menuitem']",
    )
