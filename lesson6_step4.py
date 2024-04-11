"""
#  Вариант через XPATHс получением алереа с кодом в проинте:

from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
browser.find_element('xpath', '//input[@name="first_name"]').send_keys("Ivan")
browser.find_element('xpath', '//input[@name="last_name"]').send_keys("Petrov")
browser.find_element('xpath', '//input[@class="form-control city"]').send_keys("Smolensk")
browser.find_element('xpath', '//input[@id="country"]').send_keys("Russia")
browser.find_element('xpath', '//button[@id="submit_button"]').click()
print(browser.switch_to.alert.text)
browser.quit()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

