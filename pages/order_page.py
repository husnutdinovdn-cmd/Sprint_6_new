"""Page Object для страницы заказа самоката"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators


class OrderPage:
    """Класс для работы со страницей заказа самоката"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page_load(self):
        """Ожидает загрузки страницы заказа"""
        self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.NAME_INPUT)
        )

    def fill_step1(self, name: str, surname: str, address: str,
                   metro_station: str, phone: str):
        """Заполняет первый шаг формы заказа"""
        self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.NAME_INPUT)
        ).send_keys(name)

        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)

        # Выбор станции метро
        metro_input = self.driver.find_element(*OrderPageLocators.METRO_DROPDOWN)
        metro_input.click()
        metro_input.send_keys(metro_station)
        # Выбираем опцию по названию станции или первую доступную
        try:
            option_locator = (
                OrderPageLocators.METRO_OPTION[0],
                OrderPageLocators.METRO_OPTION[1].format(metro_station)
            )
            self.wait.until(
                EC.element_to_be_clickable(option_locator)
            ).click()
        except Exception:
            self.wait.until(
                EC.element_to_be_clickable(OrderPageLocators.METRO_FIRST_OPTION)
            ).click()

        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_step2(self, date: str, rental_period: str, color: str,
                   comment: str = ""):
        """Заполняет второй шаг формы заказа"""
        self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.DATE_INPUT)
        ).send_keys(date)

        # Выбор срока аренды
        period_dropdown = self.driver.find_element(
            *OrderPageLocators.RENTAL_PERIOD_DROPDOWN
        )
        period_dropdown.click()
        option_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(rental_period)
        )
        self.wait.until(
            EC.element_to_be_clickable(option_locator)
        ).click()

        # Выбор цвета
        if color.lower() == "black" or color == "чёрный":
            self.driver.find_element(*OrderPageLocators.COLOR_BLACK_CHECKBOX).click()
        elif color.lower() == "grey" or color == "серый":
            self.driver.find_element(*OrderPageLocators.COLOR_GREY_CHECKBOX).click()

        if comment:
            self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def confirm_order(self):
        """Подтверждает заказ в модальном окне"""
        self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        ).click()

    def is_success_modal_displayed(self) -> bool:
        """Проверяет отображение модального окна об успешном заказе"""
        try:
            modal = self.wait.until(
                EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL)
            )
            return modal.is_displayed()
        except Exception:
            return False

    def get_success_modal_text(self) -> str:
        """Возвращает текст заголовка модального окна успеха"""
        header = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL_HEADER)
        )
        return header.text
