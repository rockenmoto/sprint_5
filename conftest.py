import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Метод для инициализации драйвера
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


# Метод для открытия главной страницы
@pytest.fixture()
def get_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")


# Метод для открытия страницы регистрации
@pytest.fixture()
def get_register_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")


# Метод для открытия страницы восстановления пароля
@pytest.fixture()
def get_forgot_password_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
