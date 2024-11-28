import pytest
from pages.main_page import MainPage
import data
from urls import Urls
import allure


@allure.title("Тесты на проверку вопросов и ответов на главной странице")
class TestQuestionsAndAnswer:

    @pytest.mark.parametrize(
       'num, expected_result',
       [ (0, data.answer_list[0]),
         (1, data.answer_list[1]),
         (2, data.answer_list[2]),
         (3, data.answer_list[3]),
         (4, data.answer_list[4]),
         (5, data.answer_list[5]),
         (6, data.answer_list[6]),
         (7, data.answer_list[7]),
       ]
    )
    def test_questions_and_answers(self, driver, num, expected_result):
        main_page = MainPage(driver)
        main_page.get_page(Urls.URL_SCOOTER_MAIN_PAGE)
        main_page.click_cookies_ok_button()
        main_page.check_question_and_answer(num, expected_result)





