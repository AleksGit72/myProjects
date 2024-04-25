import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #  Нажать на кнопку "I want to go on a magical journey!" через CSS_SELECTOR.
    browser.find_element(By.CSS_SELECTOR, "button").click()

    #   согласиться с сообщением
    confirm = browser.switch_to.alert
    confirm.accept()

    #  Считать значение для переменной var:
    x = browser.find_element('xpath', '//*[@id="input_value"]').text

    #  Посчитать математическую функцию от var
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    browser.find_element(By.ID, "answer").send_keys(y)

    #  Нажать на кнопку Submit через xpath.
    # browser.find_element('xpath', '/html/body/div/form/button').click()

    #  Нажать на кнопку Submit через CSS_SELECTOR.
    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
