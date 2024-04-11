"""
#  Вариант через XPATH с получением алерта с кодом в проинте:

from selenium import webdriver
from math import pi, e, ceil

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
text = str(ceil(pow(pi, e)*10000))
browser.find_element('xpath', f'//a[contains(text(),{text})]').click()
browser.find_element('xpath', '//input[@name="first_name"]').send_keys("Ivan")
browser.find_element('xpath', '//input[@name="last_name"]').send_keys("Petrov")
browser.find_element('xpath', '//input[@class="form-control city"]').send_keys("Smolensk")
browser.find_element('xpath', '//input[@id="country"]').send_keys("Russia")
browser.find_element('xpath', '//button[@class="btn btn-default"]').click()
print(browser.switch_to.alert.text)
browser.quit()

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.LINK_TEXT, "224592").click()
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "form-control.city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
