from selenium.webdriver.common.by import By

class OrderPageLocators:

    ORDER_FIRST_NAME          = By.XPATH, ".//input[@placeholder='* Имя']"
    ORDER_LAST_NAME           = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ORDER_ADDRESS             = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    ORDER_METRO_STATION       = By.XPATH, ".//input[@placeholder='* Станция метро']"
    ORDER_METRO_LIST = By.XPATH, ".//div[@class='select-search__select']/ul/li[1]/button/div[2]"
    ORDER_TEL_NO              = By.XPATH, ".//input[@placeholder ='* Телефон: на него позвонит курьер']"
    ORDER_NEXT_BUTTON         = By.XPATH, ".//button[text() = 'Далее']"

    ORDER_RENT_DATE           = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"
    ORDER_SEL_DATE            = By.XPATH, ".//div[@class = 'react-datepicker']//div[@tabindex = '0']"
    ORDER_RENT_PERIOD         = By.XPATH, ".//span[@class = 'Dropdown-arrow']"
    ORDER_SEL_RENT_PERIOD     = By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='{}']"
    ORDER_SCOOTER_COLOR       = By.ID,    "{}"
    ORDER_COMMENT_FOR_COURIER = By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"
    ORDER_CREATE_BUTTON       = By.XPATH, ".//div[contains(@class, 'Order')]/button[text() = 'Заказать']"
    ORDER_APPROVE_BUTTON      = By.XPATH, ".//button[text() = 'Да']"
    ORDER_CHECK_CREATION      = By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]"
    ORDER_STATUS_BUTTON       = By.XPATH, ".//button[text() = 'Посмотреть статус']"


