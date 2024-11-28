from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION_LOCATOR             = By.XPATH, ".//div[text() = '{}']"
    ANSWER_LOCATOR               = By.XPATH, ".//div[text() = '{}']/parent::div/parent::div/div[2]/p"
    QUESTION_LOCATOR_TO_SCROLL   = (
        By.XPATH, ".//div[text() = 'Я жизу за МКАДом, привезёте?']")
    COOKIE_LOCATOR               = By.ID, "rcc-confirm-button"

    MAIN_ORDER_BUTTON = (
        (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"),
        (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")
    )