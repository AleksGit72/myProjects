from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x1, x2):
  return str(int(x1) + int(x2))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #  Считать значение для переменной x1:
    x1_element = browser.find_element('xpath', '//*[@id="num1"]')
    x1 = x1_element.text

    #  Считать значение для переменной x2:
    #  x2_element = browser.find_element('xpath', '//*[@id="num2"]')
    #  x2 = x2_element.text

    x2 = browser.find_element('xpath', '//*[@id="num2"]').text

    #  Посчитать математическую функцию от var
    y = calc(x1, x2)

    #  Выбрать ответ в дропдауне.
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)  # ищем элемент с текстом "y"

    #  Нажать на кнопку Submit через CSS_SELECTOR.
    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
