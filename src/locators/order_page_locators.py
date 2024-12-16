class OrderPageLocators:
    """Локаторы страницы оформления заказа"""

    INPUT_FIRST_NAME: tuple[str, str] = ("xpath", "//input[@wfd-id='id29']")
    INPUT_LAST_NAME: tuple[str, str] = ("xpath", "//input[@wfd-id='id30']")
    INPUT_ADDRESS: tuple[str, str] = ("xpath", "//input[@wfd-id='id31']")
    INPUT_METRO_STATION: tuple[str, str] = ("xpath", "//input[@wfd-id='id32']")
    INPUT_PHONE_NUMBER: tuple[str, str] = ("xpath", "//input[@wfd-id='id33']")
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
        "//div[@role='option']",
    )
    CHECKBOX_BLACK_SCOOTER: tuple[str, str] = (
        "xpath",
        "//input[@wfd-id='id36']",
    )
    CHECKBOX_GRAY_SCOOTER: tuple[str, str] = (
        "xpath",
        "//input[@wfd-id='id37']",
    )
    BUTTON_ORDER: tuple[str, str] = (
        "xpath",
        "//input[@wfd-id='id38']",
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
