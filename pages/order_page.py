from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):


    def set_metro_station(self,metro_station):
        self.add_text_to_element(OrderPageLocators.ORDER_METRO_STATION, metro_station)
        self.click_to_element(OrderPageLocators.ORDER_METRO_LIST)

    def set_rent_date(self, date):
        self.add_text_to_element(OrderPageLocators.ORDER_RENT_DATE, date)
        self.click_to_element(OrderPageLocators.ORDER_SEL_DATE)

    def set_rent_period(self, period):
        self.click_to_element(OrderPageLocators.ORDER_RENT_PERIOD)
        locator_1 = self.format_locators_text(OrderPageLocators.ORDER_SEL_RENT_PERIOD, period)
        self.click_to_element(locator_1)

    def set_scooter_color(self, color):
        locator_1 = self.format_locators_text(OrderPageLocators.ORDER_SCOOTER_COLOR, color)
        self.click_to_element(locator_1)

    @allure.step('Проверяем создание данных заказчика, вариант {order_data[0]}')
    def set_customer_data(self, order_data):
        self.add_text_to_element(OrderPageLocators.ORDER_FIRST_NAME, order_data[1])
        self.add_text_to_element(OrderPageLocators.ORDER_LAST_NAME,  order_data[2])
        self.add_text_to_element(OrderPageLocators.ORDER_ADDRESS,    order_data[3])
        self.add_text_to_element(OrderPageLocators.ORDER_TEL_NO,     order_data[5])
        self.set_metro_station(order_data[4])
        self.click_to_element(OrderPageLocators.ORDER_NEXT_BUTTON)

    @allure.step('Проверяем создание данных аренды, вариант {order_data[0]}')
    def set_rent_data(self, order_data):
        self.set_rent_date(order_data[6])
        self.set_rent_period(order_data[7])
        self.set_scooter_color(order_data[8])
        self.add_text_to_element(OrderPageLocators.ORDER_COMMENT_FOR_COURIER, order_data[9])
        self.click_to_element(OrderPageLocators.ORDER_CREATE_BUTTON)

    @allure.step('Выполняем проверку оформления заказа, вариант {num}')
    def approve_and_check_order(self, num):
        self.click_to_element(OrderPageLocators.ORDER_APPROVE_BUTTON)
        assert 'Заказ оформлен' in self.get_text_from_element(OrderPageLocators.ORDER_CHECK_CREATION)
        self.click_to_element(OrderPageLocators.ORDER_STATUS_BUTTON)

    @allure.step('Тестируем оформление заказа самоката, вариант {order_data[0]}')
    def create_and_check_order(self, order_data):
        self.set_customer_data(order_data)
        self.set_rent_data(order_data)
        self.approve_and_check_order(order_data[0])



