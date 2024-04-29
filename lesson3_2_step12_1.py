import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLinks(unittest.TestCase):

    def reg_form(self, lnk):
        browser = webdriver.Chrome()
        browser.get(lnk)
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("abc@gmail.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        return browser.find_element(By.TAG_NAME, "h1").text

    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        text_expected = "Congratulations! You have successfully registered!"
        self.assertEqual(self.reg_form(link), text_expected, "Should be expected text")

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        text_expected = "Congratulations! You have successfully registered!"
        self.assertEqual(self.reg_form(link), text_expected, "Should be expected text")

if __name__ == "__main__":
    unittest.main()
