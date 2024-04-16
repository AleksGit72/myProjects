import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #  Считать значение для переменной x:
    x_element = browser.find_element('xpath', '//*[@id="treasure"]')
    x = x_element.get_attribute("valuex")

    #  Посчитать математическую функцию от x
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    browser.find_element(By.ID, "answer").send_keys(y)

    #  Отметить checkbox "I'm the robot".
    browser.find_element(By.ID, "robotCheckbox").click()

    #  Выбрать radiobutton "Robots rule!".
    browser.find_element(By.ID, "robotsRule").click()

    #  Нажать на кнопку Submit через xpath.
    # browser.find_element('xpath', '/html/body/div/form/button').click()

    #  Нажать на кнопку Submit через CSS_SELECTOR.
    browser.find_element(By.CSS_SELECTOR, "button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
