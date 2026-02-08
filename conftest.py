"""
Фикстуры pytest для автотестов Яндекс.Самокат
"""
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    """Добавляет опции командной строки для pytest"""
    parser.addoption(
        '--browser',
        action='store',
        default='firefox',
        help='Выбор браузера: firefox или chrome'
    )
    parser.addoption(
        '--headless',
        action='store_true',
        default=False,
        help='Запуск в headless режиме'
    )


@pytest.fixture(scope='function')
def browser(request):
    """
    Фикстура для создания и закрытия браузера.
    По заданию используется Firefox.
    """
    browser_name = request.config.getoption('--browser', default='firefox')
    headless = request.config.getoption('--headless', default=False)

    if browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument('--headless')
        firefox_options.set_preference('dom.webdriver.enabled', False)
        
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
    else:
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        from webdriver_manager.chrome import ChromeDriverManager
        
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
        
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
