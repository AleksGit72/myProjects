import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #  Нажать на кнопку "I want to go on a magical journey!" через CSS_SELECTOR.
    browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary").click()

    #  Переключиться на новую вкладку 1 вариант
    #  new_window = browser.window_handles[1]
    #  browser.switch_to.window(new_window)

    #  Переключиться на новую вкладку 2 вариант
    lst = browser.window_handles
    browser.switch_to.window(lst[1])
    #  print(*lst)

    #  Считать значение для переменной var:
    x = browser.find_element('xpath', '//*[@id="input_value"]').text

    #  Посчитать математическую функцию от var
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    browser.find_element(By.ID, "answer").send_keys(y)

    #  Нажать на кнопку Submit через CSS_SELECTOR.
    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    print(browser.switch_to.alert.text.split()[-1])
    time.sleep(10)
    #  закрываем браузер после всех манипуляций
    browser.quit()
