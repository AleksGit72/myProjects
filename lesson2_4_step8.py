import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def calc(var):
    return str(math.log(abs(12 * math.sin(int(var)))))


try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium ждать в течение 15 секунд, пока появится нужное значение
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    # найти кнопку подтверждения решения
    submit_button = browser.find_element (By.ID, 'solve')

    # проскроллить до кнопки подтверждения решения
    browser.execute_script('return arguments[0].scrollIntoView(true);', submit_button)

    #  Считать значение для переменной var:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    browser.find_element(By.ID, "answer").send_keys(y)

    #  подтвердить ввод решения.
    submit_button.click()


finally:

    print(browser.switch_to.alert.text.split()[-1])
    #  ожидание чтобы визуально оценить результаты прохождения скрипта
    #  time.sleep(10)

    #  закрываем браузер после всех манипуляций
    browser.quit()
