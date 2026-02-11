"""
Тесты заказа самоката - позитивный сценарий
Проверка полного флоу с двумя наборами данных и двумя точками входа
"""
import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA_SET_1, ORDER_DATA_SET_2


@allure.feature('Заказ самоката')
@allure.story('Позитивный сценарий заказа')
class TestOrder:
    """Тесты процесса заказа самоката"""

    @pytest.mark.parametrize('order_data', [ORDER_DATA_SET_1, ORDER_DATA_SET_2],
                             ids=['Набор данных 1', 'Набор данных 2'])
    @allure.title('Успешный заказ через верхнюю кнопку "Заказать"')
    def test_successful_order_via_header_button(self, browser, order_data):
        """
        Позитивный сценарий заказа через верхнюю кнопку:
        1. Нажать кнопку Заказать в шапке
        2. Заполнить форму заказа
        3. Проверить появление всплывающего окна об успешном создании заказа
        """
        main_page = MainPage(browser)
        order_page = OrderPage(browser)

        main_page.open()
        main_page.accept_cookies()

        # Клик на верхнюю кнопку Заказать
        main_page.click_order_button_header()

        order_page.wait_for_page_load()

        # Заполнение первого шага
        order_page.fill_step1(
            name=order_data['name'],
            surname=order_data['surname'],
            address=order_data['address'],
            metro_station=order_data['metro_station'],
            phone=order_data['phone']
        )

        # Заполнение второго шага
        order_page.fill_step2(
            date=order_data['date'],
            rental_period=order_data['rental_period'],
            color=order_data['color'],
            comment=order_data.get('comment', '')
        )

        # Подтверждение заказа
        order_page.confirm_order()

        # Проверка модального окна успеха
        assert order_page.is_success_modal_displayed(), (
            "Ожидалось появление модального окна об успешном создании заказа"
        )
        modal_text = order_page.get_success_modal_text()
        assert "Заказ оформлен" in modal_text or "Номер заказа" in modal_text, (
            f"Текст модального окна должен содержать информацию об успехе. "
            f"Получено: {modal_text}"
        )

    @pytest.mark.parametrize('order_data', [ORDER_DATA_SET_1, ORDER_DATA_SET_2],
                             ids=['Набор данных 1', 'Набор данных 2'])
    @allure.title('Успешный заказ через нижнюю кнопку "Заказать"')
    def test_successful_order_via_bottom_button(self, browser, order_data):
        """
        Позитивный сценарий заказа через нижнюю кнопку:
        1. Прокрутить к нижней кнопке Заказать
        2. Нажать кнопку Заказать внизу страницы
        3. Заполнить форму заказа
        4. Проверить появление всплывающего окна об успешном создании заказа
        """
        main_page = MainPage(browser)
        order_page = OrderPage(browser)

        main_page.open()
        main_page.accept_cookies()

        # Прокрутка и клик на нижнюю кнопку Заказать
        main_page.scroll_to_bottom_order_button()
        main_page.click_order_button_bottom()

        order_page.wait_for_page_load()

        # Заполнение первого шага
        order_page.fill_step1(
            name=order_data['name'],
            surname=order_data['surname'],
            address=order_data['address'],
            metro_station=order_data['metro_station'],
            phone=order_data['phone']
        )

        # Заполнение второго шага
        order_page.fill_step2(
            date=order_data['date'],
            rental_period=order_data['rental_period'],
            color=order_data['color'],
            comment=order_data.get('comment', '')
        )

        # Подтверждение заказа
        order_page.confirm_order()

        # Проверка модального окна успеха
        assert order_page.is_success_modal_displayed(), (
            "Ожидалось появление модального окна об успешном создании заказа"
        )
        modal_text = order_page.get_success_modal_text()
        assert "Заказ оформлен" in modal_text or "Номер заказа" in modal_text, (
            f"Текст модального окна должен содержать информацию об успехе. "
            f"Получено: {modal_text}"
        )
