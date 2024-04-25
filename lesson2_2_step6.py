import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

#  Считать значение для переменной var:
x_element = browser.find_element('xpath', '//*[@id="input_value"]')
x = x_element.text
y = calc(x)


#  Ввести ответ в текстовое поле.
browser.find_element(By.ID, "answer").send_keys(y)

#  Отметить checkbox "I'm the robot".
browser.find_element(By.ID, "robotCheckbox").click()

#  Выбрать radiobutton "Robots rule!".
radio_btn = browser.find_element(By.ID, "robotsRule")
# прокрутка страницы
browser.execute_script("window.scrollBy(0, 100);", radio_btn)  # scrolling by 100 px
radio_btn.click()

#  Нажать на кнопку Submit через CSS_SELECTOR.
button = browser.find_element(By.TAG_NAME, "button")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
