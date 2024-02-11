import pytest
from selenium import webdriver


# Метод для инициализации драйвера
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


# Метод для открытия главной страницы
@pytest.fixture()
def get_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
