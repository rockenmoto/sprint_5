from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

USER_LOGIN_DATA = {
    'email': 'kirill_belov_666@yandex.ru',
    'password': 'yandexPractikumRulit'
}


def test_login_from_sign_in_button_true(driver, get_main_page):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))

    email_input = driver.find_element(By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    email_input.send_keys(USER_LOGIN_DATA['email'])

    password_input = driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    password_input.send_keys(USER_LOGIN_DATA['password'])

    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

    assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/button[text()="Оформить '
                                                                                      'заказ"]')))
    driver.quit()


def test_login_from_personal_profile_button_true(driver, get_main_page):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))

    email_input = driver.find_element(By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    email_input.send_keys(USER_LOGIN_DATA['email'])

    password_input = driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    password_input.send_keys(USER_LOGIN_DATA['password'])

    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

    assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/button[text()="Оформить '
                                                                                      'заказ"]')))
    driver.quit()


def test_login_from_register_button_true(driver, get_register_page):
    driver.find_element(By.XPATH, './/a[text()="Войти"]').click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))

    email_input = driver.find_element(By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    email_input.send_keys(USER_LOGIN_DATA['email'])

    password_input = driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    password_input.send_keys(USER_LOGIN_DATA['password'])

    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

    assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/button[text()="Оформить '
                                                                                      'заказ"]')))
    driver.quit()


def test_login_from_forgot_pass_button_true(driver, get_forgot_password_page):
    driver.find_element(By.XPATH, './/a[text()="Войти"]').click()
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, './/button[text()="Войти"]')))

    email_input = driver.find_element(By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    email_input.send_keys(USER_LOGIN_DATA['email'])

    password_input = driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    password_input.send_keys(USER_LOGIN_DATA['password'])

    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

    assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, './/button[text()="Оформить '
                                                                                      'заказ"]')))
    driver.quit()
