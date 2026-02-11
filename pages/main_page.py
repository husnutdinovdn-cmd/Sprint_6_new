"""Page Object для главной страницы Яндекс.Самокат"""
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL


class MainPage(BasePage):
    """Класс для работы с главной страницей Яндекс.Самокат"""

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = BASE_URL

    @allure.step("Открыть главную страницу")
    def open(self):
        """Открывает главную страницу"""
        self.open_url(self.base_url)
        self.wait_for_page_load()

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_page_load(self):
        """Ожидает загрузки главной страницы"""
        self.wait_for_element_present(MainPageLocators.HOME_PAGE_CONTAINER)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        """Принимает cookies если отображается баннер"""
        try:
            if self.is_element_displayed(MainPageLocators.COOKIE_CONFIRM_BUTTON):
                self.click_element(MainPageLocators.COOKIE_CONFIRM_BUTTON)
        except Exception:
            pass

    @allure.step("Кликнуть на кнопку 'Заказать' в шапке")
    def click_order_button_header(self):
        """Кликает на кнопку 'Заказать' в шапке страницы"""
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Кликнуть на кнопку 'Заказать' внизу страницы")
    def click_order_button_bottom(self):
        """Кликает на кнопку 'Заказать' внизу страницы"""
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Прокрутить к разделу FAQ")
    def scroll_to_faq(self):
        """Прокручивает страницу к разделу FAQ"""
        self.scroll_to_element(MainPageLocators.FAQ_ACCORDION)

    @allure.step("Прокрутить к нижней кнопке заказа")
    def scroll_to_bottom_order_button(self):
        """Прокручивает страницу к нижней кнопке заказа"""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть на вопрос FAQ #{index}")
    def click_faq_question(self, index: int):
        """Кликает на вопрос в FAQ по индексу (0-7)"""
        locator = (
            By.ID,
            MainPageLocators.FAQ_QUESTION[1].format(index)
        )
        self.click_element(locator)

    @allure.step("Получить текст ответа FAQ #{index}")
    def get_faq_answer_text(self, index: int) -> str:
        """Возвращает текст ответа на вопрос FAQ по индексу"""
        locator = (By.ID, MainPageLocators.FAQ_ANSWER[1].format(index))
        return self.get_element_text(locator)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        """Кликает на логотип Яндекса"""
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        """Кликает на логотип Самоката"""
        self.click_element(MainPageLocators.SCOOTER_LOGO)
