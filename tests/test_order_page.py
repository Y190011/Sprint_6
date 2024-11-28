import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
import data
from urls import Urls
import allure


@allure.title("Тесты на проверку создания ордеров и переходов")
class TestOrderCreate:

    @pytest.mark.parametrize(
        'order_data',
        [
            data.order_data_variants[0],
            data.order_data_variants[1]
         ]
    )

    def test_create_order(self, driver, order_data):
        test_number     = order_data[0]
        main_page       = MainPage(driver)
        order_page      = OrderPage(driver)

        main_page.get_page(Urls.URL_SCOOTER_MAIN_PAGE)
        main_page.click_cookies_ok_button()

        main_page.click_to_order_button(test_number)
        order_page.create_and_check_order(order_data)





