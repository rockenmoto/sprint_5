import pytest
from selenium import webdriver


# Метод для инициализации драйвера
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


# Метод для открытия главной страницы
@pytest.fixture(scope="function")
def get_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")


# Метод для открытия страницы регистрации
@pytest.fixture(scope="function")
def get_register_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")


# Метод для открытия страницы восстановления пароля
@pytest.fixture(scope="function")
def get_forgot_password_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
