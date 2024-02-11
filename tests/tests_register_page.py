import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *


def test_register_user_valid_values_true(driver, get_main_page):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    name = 'Test'
    email = f'kirill_belov_{random.randint(0, 100)}@yandex.ru'
    password = 'yandexPractikumRulit'

    name_input = driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input")
    name_input.send_keys(name)

    email_input = driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input")
    email_input.send_keys(email)

    password_input = driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input")
    password_input.send_keys(password)

    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()

    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))
    assert '/login' in driver.current_url

    driver.quit()


def test_register_user_invalid_email_false(driver, get_main_page):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    name = 'Test'
    email = f'kirill_belov_{random.randint(0, 100)}@yandex.ru'
    password = f'{random.randint(0, 100)}'

    name_input = driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input")
    name_input.send_keys(name)

    email_input = driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input")
    email_input.send_keys(email)

    password_input = driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input")
    password_input.send_keys(password)

    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()

    error_message = WebDriverWait(driver, 3).until(
        ec.visibility_of_element_located((By.XPATH, ".//p[@class ='input__error text_type_main-default']"))).text
    assert "Некорректный пароль" == error_message

    driver.quit()
