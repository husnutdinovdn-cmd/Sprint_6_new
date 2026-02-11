"""Базовый класс для всех Page Object"""
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс для всех страниц с общими методами работы с WebDriver"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть URL: {url}")
    def open_url(self, url: str):
        """Открывает указанный URL"""
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        """Возвращает текущий URL страницы"""
        return self.driver.current_url

    @allure.step("Ожидание присутствия элемента")
    def wait_for_element_present(self, locator: tuple, timeout: int = 10):
        """Ожидает присутствия элемента в DOM"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator: tuple, timeout: int = 10):
        """Ожидает видимости элемента на странице"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_clickable(self, locator: tuple, timeout: int = 10):
        """Ожидает, что элемент станет кликабельным"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Найти элемент")
    def find_element(self, locator: tuple):
        """Находит элемент по локатору"""
        return self.driver.find_element(*locator)

    @allure.step("Найти элементы")
    def find_elements(self, locator: tuple):
        """Находит все элементы по локатору"""
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator: tuple):
        """Кликает на элемент после ожидания его кликабельности"""
        element = self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Ввести текст в элемент")
    def send_keys_to_element(self, locator: tuple, text: str):
        """Вводит текст в элемент"""
        element = self.wait_for_element_present(locator)
        element.send_keys(text)

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, locator: tuple):
        """Прокручивает страницу к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script: str, *args):
        """Выполняет JavaScript код"""
        return self.driver.execute_script(script, *args)

    @allure.step("Проверить отображение элемента")
    def is_element_displayed(self, locator: tuple) -> bool:
        """Проверяет, отображается ли элемент на странице"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except Exception:
            return False

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator: tuple) -> str:
        """Возвращает текст элемента"""
        element = self.wait_for_element_visible(locator)
        return element.text

    @allure.step("Получить список открытых окон")
    def get_window_handles(self) -> list:
        """Возвращает список дескрипторов всех открытых окон"""
        return self.driver.window_handles

    @allure.step("Переключиться на окно")
    def switch_to_window(self, window_handle: str):
        """Переключается на указанное окно"""
        self.driver.switch_to.window(window_handle)

    @allure.step("Ожидание появления нового окна")
    def wait_for_new_window(self, initial_windows: list, timeout: int = 10):
        """Ожидает появления нового окна/вкладки"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: len(driver.window_handles) > len(initial_windows))
        return self.driver.window_handles
