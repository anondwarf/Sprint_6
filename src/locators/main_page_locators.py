class MainPageLocators:
    """Локаторы `MainPage`"""

    DIV_ACCORTION_HEADER: tuple[str, str] = (
        "xpath",
        "//div[contains(text(), 'Вопросы о важном')]",
    )
    DIV_ACCORDION_BUTTON: tuple[str, str] = (
        "xpath",
        "//div[@class='accordion__button']",
    )
    P_ACCORDION: tuple[str, str] = (
        "xpath",
        "//div[@class='accordion__panel']//p",
    )
