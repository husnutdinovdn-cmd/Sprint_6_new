"""
Тесты навигации по логотипам
"""
import allure

from pages.main_page import MainPage
from urls import BASE_URL, YANDEX_DZEN_URL, YANDEX_URL


@allure.feature('Навигация')
@allure.story('Логотипы')
class TestLogoNavigation:
    """Тесты переходов по логотипам"""

    @allure.title('Логотип Самоката ведёт на главную страницу')
    def test_scooter_logo_opens_main_page(self, browser):
        """
        Проверяет: при клике на логотип Самоката открывается главная страница.
        """
        main_page = MainPage(browser)
        main_page.open()
        main_page.accept_cookies()

        # Переходим на страницу заказа
        main_page.click_order_button_header()
        order_url = main_page.get_current_url()
        assert "order" in order_url, "Должны находиться на странице заказа"

        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()

        # Проверяем, что вернулись на главную
        current_url = main_page.get_current_url()
        assert BASE_URL == current_url, (
            f"Ожидалась главная страница Самоката {BASE_URL}. Текущий URL: {current_url}"
        )

    @allure.title('Логотип Яндекса открывает Дзен в новом окне')
    def test_yandex_logo_opens_dzen(self, browser):
        """
        Проверяет: при клике на логотип Яндекса в новом окне
        через редирект открывается главная страница Дзена.
        """
        main_page = MainPage(browser)
        main_page.open()
        main_page.accept_cookies()

        initial_windows = main_page.get_window_handles()

        # Кликаем на логотип Яндекса (открывается в новой вкладке)
        main_page.click_yandex_logo()

        # Ожидаем появления нового окна
        new_windows = main_page.wait_for_new_window(initial_windows)

        assert len(new_windows) > len(initial_windows), (
            "Ожидалось открытие новой вкладки/окна"
        )

        # Переключаемся на новое окно
        main_page.switch_to_window(new_windows[-1])
        current_url = main_page.get_current_url()

        # Дзен может быть на dzen.ru или yandex.ru с редиректом
        assert YANDEX_DZEN_URL in current_url or YANDEX_URL in current_url, (
            f"Ожидался переход на Дзен/Яндекс. Текущий URL: {current_url}"
        )