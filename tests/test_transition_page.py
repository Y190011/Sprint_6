import pytest
from pages.transition_page import TransitionPage
#import data
from urls import Urls
import allure


@allure.title("Тесты на переходы")
class TestTransition:

    @pytest.mark.parametrize(
        'num', [0, 1],
          )

    def test_transition(self, driver, num):
        test_transition_page = TransitionPage(driver)
        test_transition_page.get_page(Urls.URL_PAGE_FOR_TRANSITION)
        test_transition_page.transition_to(num)
        test_transition_page.check_transition(num)