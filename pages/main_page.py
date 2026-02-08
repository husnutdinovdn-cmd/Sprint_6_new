"""Page Object для главной страницы Яндекс.Самокат"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators


class MainPage:
    """Класс для работы с главной страницей Яндекс.Самокат"""

    def __init__(self, driver):
        self.driver = driver
        self.base_url = MainPageLocators.BASE_URL
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открывает главную страницу"""
        self.driver.get(self.base_url)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        """Ожидает загрузки главной страницы"""
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'Home_HomePage')]")
        ))

    def accept_cookies(self):
        """Принимает cookies если отображается баннер"""
        try:
            cookie_btn = self.driver.find_element(
                *MainPageLocators.COOKIE_CONFIRM_BUTTON
            )
            if cookie_btn.is_displayed():
                cookie_btn.click()
        except Exception:
            pass

    def click_order_button_header(self):
        """Кликает на кнопку 'Заказать' в шапке страницы"""
        order_btn = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
        )
        order_btn.click()

    def click_order_button_bottom(self):
        """Кликает на кнопку 'Заказать' внизу страницы"""
        order_btn = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)
        )
        order_btn.click()

    def scroll_to_faq(self):
        """Прокручивает страницу к разделу FAQ"""
        faq = self.driver.find_element(*MainPageLocators.FAQ_ACCORDION)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)

    def scroll_to_bottom_order_button(self):
        """Прокручивает страницу к нижней кнопке заказа"""
        order_btn = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_btn)

    def click_faq_question(self, index: int):
        """Кликает на вопрос в FAQ по индексу (0-7)"""
        locator = (
            By.ID,
            MainPageLocators.FAQ_QUESTION[1].format(index)
        )
        question = self.wait.until(EC.element_to_be_clickable(locator))
        question.click()

    def get_faq_answer_text(self, index: int) -> str:
        """Возвращает текст ответа на вопрос FAQ по индексу"""
        locator = (By.ID, MainPageLocators.FAQ_ANSWER[1].format(index))
        answer = self.wait.until(EC.presence_of_element_located(locator))
        return answer.text

    def click_yandex_logo(self):
        """Кликает на логотип Яндекса"""
        logo = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        )
        logo.click()

    def click_scooter_logo(self):
        """Кликает на логотип Самоката"""
        logo = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)
        )
        logo.click()

    def get_current_url(self) -> str:
        """Возвращает текущий URL"""
        return self.driver.current_url
