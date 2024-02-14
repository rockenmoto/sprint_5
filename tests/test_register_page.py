import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

VALID_USER_DATA = {
    'name': 'Test',
    'email': f'kirill_belov_{random.randint(0, 100)}@yandex.ru',
    'password': 'yandexPractikumRulit'
}

INVALID_PASSWORD = '123'


def test_register_user_valid_values_true(driver, get_register_page):
    name_input = driver.find_element(By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")
    name_input.send_keys(VALID_USER_DATA['name'])

    email_input = driver.find_element(By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    email_input.send_keys(VALID_USER_DATA['email'])

    password_input = driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    password_input.send_keys(VALID_USER_DATA['password'])

    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()

    assert WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))
    driver.quit()


def test_register_user_invalid_email_false(driver, get_register_page):
    name_input = driver.find_element(By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")
    name_input.send_keys(VALID_USER_DATA['name'])

    email_input = driver.find_element(By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    email_input.send_keys(VALID_USER_DATA['email'])

    password_input = driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    password_input.send_keys(INVALID_PASSWORD)

    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()

    assert WebDriverWait(driver, 3).until(
        ec.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']"))).text
    driver.quit()
