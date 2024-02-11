from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *

USER_LOGIN_DATA = {
    'email': 'kirill_belov_666@yandex.ru',
    'password': 'yandexPractikumRulit'
}


def test_open_main_page_from_header_logo_true(driver, get_main_page):
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

    driver.find_element(By.XPATH, './/a[@href = "/"]').click()
    assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/button[text()="Оформить '
                                                                                      'заказ"]')))
    driver.quit()


def test_open_main_page_from_constructor_logo_true(driver, get_main_page):
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

    driver.find_element(By.XPATH, './/p[text() = "Конструктор"]').click()
    assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/button[text()="Оформить '
                                                                                      'заказ"]')))
    driver.quit()


def test_open_buns_section_true(driver, get_main_page):
    # Для проверки перехода в секцию булки, вначале выбираем раздел "Соусы"
    driver.find_element(By.XPATH, './/span[text() = "Соусы"]').click()

    driver.find_element(By.XPATH, './/span[text() = "Булки"]').click()
    # Проверяем выбранный раздел
    assert 'current__2BEPc' in driver.find_element(By.XPATH, './/div[@style ="display: flex;"]/div[1]').get_attribute(
        'class')
    # Проверяем видимость элемента
    assert driver.find_element(
        By.XPATH, './/img[@src="https://code.s3.yandex.net/react/code/bun-01.png"]').is_displayed()
    driver.quit()


def test_open_sauce_section_true(driver, get_main_page):
    driver.find_element(By.XPATH, './/span[text() = "Соусы"]').click()
    # Проверяем выбранный раздел
    assert 'current__2BEPc' in driver.find_element(By.XPATH, './/div[@style ="display: flex;"]/div[2]').get_attribute(
        'class')
    # Проверяем видимость элемента
    assert driver.find_element(
        By.XPATH, './/img[@src="https://code.s3.yandex.net/react/code/sauce-02.png"]').is_displayed()

    driver.quit()


def test_open_toppings_section_true(driver, get_main_page):
    driver.find_element(By.XPATH, './/span[text() = "Начинки"]').click()
    # Проверяем выбранный раздел
    assert 'current__2BEPc' in driver.find_element(By.XPATH, './/div[@style ="display: flex;"]/div[3]').get_attribute(
        'class')
    # Проверяем видимость элемента
    assert driver.find_element(
        By.XPATH, './/img[@src="https://code.s3.yandex.net/react/code/meat-02.png"]').is_displayed()
    driver.quit()
