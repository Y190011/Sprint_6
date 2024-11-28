from selenium.webdriver.common.by import By

class TransitionPageLocators:

    GOTO_SCOOTER_SITE_URL = By.XPATH, "//img[@alt='Scooter']"
    GOTO_YANDEX_SITE_URL = By.XPATH, "//img[@alt='Yandex']"

    TUPLE_FOR_PARAMETRIZATION_TRANSITION = GOTO_SCOOTER_SITE_URL, GOTO_YANDEX_SITE_URL

    CHECK_SCOOTER_SITE = By.XPATH, "//div[contains(@class, 'Home_Header')]"
    CHECK_YANDEX_SITE = By.XPATH, "//button[text() = 'Найти']"

    TUPLE_FOR_PARAMETRIZATION_CHECK = ( CHECK_SCOOTER_SITE, CHECK_YANDEX_SITE )