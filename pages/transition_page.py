from locators.transition_page_locators import TransitionPageLocators
from pages.base_page import BasePage
import allure

class TransitionPage(BasePage):


    def check_site(self, num):
        self.find_element_with_wait(TransitionPageLocators.TUPLE_FOR_PARAMETRIZATION_CHECK[num])

    @allure.step("Проверяем переход, вариант {num}")
    def check_transition(self, num):
        self.switch_to_window()
        self.check_site(num)

    @allure.step("Кликаем на элемент перехода, вариант {num}")
    def transition_to(self, num):
        self.click_to_element(TransitionPageLocators.TUPLE_FOR_PARAMETRIZATION_TRANSITION[num])