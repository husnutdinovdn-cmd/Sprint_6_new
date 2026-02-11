"""Page Object для страницы заказа самоката"""
import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    """Класс для работы со страницей заказа самоката"""

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидание загрузки страницы заказа")
    def wait_for_page_load(self):
        """Ожидает загрузки страницы заказа"""
        self.wait_for_element_present(OrderPageLocators.NAME_INPUT)

    @allure.step("Заполнить первый шаг формы заказа")
    def fill_step1(self, name: str, surname: str, address: str,
                   metro_station: str, phone: str):
        """Заполняет первый шаг формы заказа"""
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)

        # Выбор станции метро
        self.click_element(OrderPageLocators.METRO_DROPDOWN)
        self.send_keys_to_element(OrderPageLocators.METRO_DROPDOWN, metro_station)
        # Выбираем опцию по названию станции или первую доступную
        try:
            option_locator = (
                OrderPageLocators.METRO_OPTION[0],
                OrderPageLocators.METRO_OPTION[1].format(metro_station)
            )
            self.click_element(option_locator)
        except Exception:
            self.click_element(OrderPageLocators.METRO_FIRST_OPTION)

        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить второй шаг формы заказа")
    def fill_step2(self, date: str, rental_period: str, color: str,
                   comment: str = ""):
        """Заполняет второй шаг формы заказа"""
        self.send_keys_to_element(OrderPageLocators.DATE_INPUT, date)

        # Выбор срока аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        option_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(rental_period)
        )
        self.click_element(option_locator)

        # Выбор цвета
        if color.lower() == "black" or color == "чёрный":
            self.click_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif color.lower() == "grey" or color == "серый":
            self.click_element(OrderPageLocators.COLOR_GREY_CHECKBOX)

        if comment:
            self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        """Подтверждает заказ в модальном окне"""
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить отображение модального окна успеха")
    def is_success_modal_displayed(self) -> bool:
        """Проверяет отображение модального окна об успешном заказе"""
        try:
            return self.wait_for_element_visible(OrderPageLocators.SUCCESS_MODAL).is_displayed()
        except Exception:
            return False

    @allure.step("Получить текст модального окна успеха")
    def get_success_modal_text(self) -> str:
        """Возвращает текст заголовка модального окна успеха"""
        return self.get_element_text(OrderPageLocators.SUCCESS_MODAL_HEADER)
