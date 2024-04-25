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

    # говорим Selenium проверять в течение 2 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    browser.execute_script("window.scrollBy(0, 300);", button)  # scrolling by 300 px down

    #  Считать значение для переменной var:
    x_element = browser.find_element('xpath', '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    #  Ввести ответ в текстовое поле.
    browser.find_element(By.ID, "answer").send_keys(y)

    #  подтвердить ввод решения.
    browser.find_element(By.ID, "solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
