
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLink(unittest.TestCase):

    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("abc@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        text_actual = browser.find_element(By.TAG_NAME, 'h1').text
        text_expected = "Congratulations! You have successfully registered!"
        self.assertEqual(text_actual, text_expected)

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("abc@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        text_actual = browser.find_element (By.TAG_NAME, 'h1').text
        text_expected = "Congratulations! You have successfully registered!"
        self.assertEqual(text_actual, text_expected)


if __name__ == "__main__":
    unittest.main()
