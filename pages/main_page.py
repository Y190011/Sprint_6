from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure
import data


class MainPage(BasePage):

    @allure.step('Клик на вопрос  {num}')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators_text(MainPageLocators.QUESTION_LOCATOR, data.questions_list[num])
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос {num}')
    def get_answer_text(self,num):
        locator_a_formatted = self.format_locators_text(MainPageLocators.ANSWER_LOCATOR, data.questions_list[num])
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Тестируем вариант {num}')
    def check_question_and_answer(self, num, expected_result):
        self.click_to_question(num)
        actual_result = self.get_answer_text(num)
        self.check_result(actual_result, expected_result, num)

    @allure.step('Проверяем ответ {num}')
    def check_result(self, actual_result, expected_result, num):
        assert actual_result == expected_result

    def click_cookies_ok_button(self):
        self.click_to_element(MainPageLocators.COOKIE_LOCATOR)

    def click_to_order_button(self,num):
        self.click_to_element(MainPageLocators.MAIN_ORDER_BUTTON[num])
