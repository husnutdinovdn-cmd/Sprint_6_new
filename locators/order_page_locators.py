"""Локаторы страницы заказа самоката"""
from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы элементов страницы заказа"""
    
    # Шаг 1 - Кто самокат
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_DROPDOWN = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__option') and contains(., '{}')]")
    METRO_FIRST_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__option')][1]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Шаг 2 - Про аренду
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-root')][.//*[contains(text(), 'Срок аренды')]]//div[contains(@class, 'Dropdown-control')]")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and contains(., '{}')]")
    # Цвет самоката - чекбоксы (могут иметь id black/grey или input с value)
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Модальное окно успешного заказа
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
