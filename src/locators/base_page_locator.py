class BasePageLocator:
    """Локаторы `BasePage`"""

    LOGO_LINK_YANDEX: tuple[str, str] = ("xpath", "//a[@href='//yandex.ru']")
    LOGO_LINK_SCOOTER: tuple[str, str] = ("xpath", "//a[@href='/']")
    BUTTON_ORDER: tuple[str, str] = (
        "xpath",
        "//div[contains(@class, 'Header_Nav')]/button[contains(text(), 'Заказать')]",
    )
