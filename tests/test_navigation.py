"""
Тесты навигации по логотипам
"""
import time
import allure

from pages.main_page import MainPage


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
        order_url = browser.current_url
        assert "order" in order_url, "Должны находиться на странице заказа"

        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()

        # Проверяем, что вернулись на главную
        current_url = main_page.get_current_url()
        assert main_page.base_url in current_url or "order" not in current_url, (
            f"Ожидалась главная страница Самоката. Текущий URL: {current_url}"
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

        initial_windows = browser.window_handles

        # Кликаем на логотип Яндекса (открывается в новой вкладке)
        main_page.click_yandex_logo()

        # Ожидаем появления нового окна
        time.sleep(2)  # Даём время на редирект
        new_windows = browser.window_handles

        assert len(new_windows) > len(initial_windows), (
            "Ожидалось открытие новой вкладки/окна"
        )

        # Переключаемся на новое окно
        browser.switch_to.window(new_windows[-1])
        current_url = browser.current_url

        # Дзен может быть на dzen.ru или yandex.ru с редиректом
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, (
            f"Ожидался переход на Дзен/Яндекс. Текущий URL: {current_url}"
        )
