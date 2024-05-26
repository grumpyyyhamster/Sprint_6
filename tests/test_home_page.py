import allure
import pytest
from conftest import driver
from data_to_use import TestData
from pages.home_page import HomePage


class TestFAQ:
    @allure.title('Набор тестов проверки раздела "Вопросы о важном"')
    @allure.description(
        'Каждый тест проверяет, что при клике на определенный вопрос - пользователь получит определенный ответ')
    @pytest.mark.parametrize('q_number, answer', TestData.FAQ_QUESTIONS_AND_ANSWERS)
    def test_faq_questions_have_right_answers(self, driver, q_number, answer):
        hp = HomePage(driver)
        hp.scroll_to_faq()
        hp.click_on_question_in_faq(q_number)
        hp.waiting_for_item_to_be_visible_faq(q_number)
        assert hp.item_text_faq(q_number) == answer
