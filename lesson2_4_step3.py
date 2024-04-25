#  import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(2)  # задать "неявное" ожидание при инициализации драйвера, чтобы применить его ко всем тестам - 2 вариант
browser.get("http://suninjuly.github.io/wait1.html")

#  time.sleep(2)  # добавляем ожидание, т.к. кнопка Verify появляется с задержкой 1 сек. - 1 вариант
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
