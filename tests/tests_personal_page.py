from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *

USER_LOGIN_DATA = {
    'email': 'kirill_belov_666@yandex.ru',
    'password': 'yandexPractikumRulit'
}


def test_open_personal_page_with_after_login_with_personal_profile_button_true(driver, get_main_page):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))

    email_input = driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input")
    email_input.send_keys(USER_LOGIN_DATA['email'])

    password_input = driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input")
    password_input.send_keys(USER_LOGIN_DATA['password'])

    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

    WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/button[text()="Оформить '
                                                                               'заказ"]')))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

    assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/a[text()="История '
                                                                                      'заказов"]')))
    driver.quit()


def test_logout_true(driver, get_main_page):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))

    email_input = driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input")
    email_input.send_keys(USER_LOGIN_DATA['email'])

    password_input = driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input")
    password_input.send_keys(USER_LOGIN_DATA['password'])

    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

    WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/button[text()="Оформить '
                                                                               'заказ"]')))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

    WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/a[text()="История '
                                                                               'заказов"]')))
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

    assert WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))
    driver.quit()
