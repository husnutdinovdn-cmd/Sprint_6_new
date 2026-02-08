"""Локаторы главной страницы Яндекс.Самокат"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов главной страницы"""
    
    # URL
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    
    # Кнопки заказа
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    # FAQ - выпадающий список "Вопросы о важном"
    FAQ_ACCORDION = (By.CLASS_NAME, "accordion")
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")  # Формат: accordion__heading-0 ... accordion__heading-7
    FAQ_ANSWER = (By.ID, "accordion__panel-{}")  # Формат: accordion__panel-0 ... accordion__panel-7
    
    # Логотипы
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    
    # Cookie consent
    COOKIE_CONFIRM_BUTTON = (By.ID, "rcc-confirm-button")
