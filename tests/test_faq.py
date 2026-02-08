"""
Тесты раздела FAQ "Вопросы о важном"
Проверка: при клике на стрелочку/вопрос открывается соответствующий текст
"""
import pytest
import allure

from pages.main_page import MainPage
from data.faq_data import FAQ_EXPECTED_ANSWERS


@allure.feature('FAQ')
@allure.story('Выпадающий список "Вопросы о важном"')
class TestFAQ:
    """Тесты для FAQ аккордеона"""

    @pytest.mark.parametrize('question_index', list(FAQ_EXPECTED_ANSWERS.keys()))
    @allure.title('Вопрос #{question_index}: отображается корректный ответ')
    def test_faq_question_opens_correct_answer(self, browser, question_index):
        """
        Проверяет, что при клике на вопрос открывается соответствующий текст ответа.
        Отдельный тест на каждый из 8 вопросов.
        """
        main_page = MainPage(browser)
        main_page.open()
        main_page.accept_cookies()
        main_page.scroll_to_faq()

        # Кликаем на вопрос
        main_page.click_faq_question(question_index)

        # Получаем текст ответа
        answer_text = main_page.get_faq_answer_text(question_index)

        # Проверяем, что ожидаемый текст содержится в ответе
        expected_substring = FAQ_EXPECTED_ANSWERS[question_index]
        assert expected_substring in answer_text, (
            f"Ожидалось, что ответ содержит '{expected_substring}', "
            f"получено: '{answer_text}'"
        )
