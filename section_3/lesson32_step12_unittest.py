from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def registration(self, website):
        browser = webdriver.Chrome()
        browser.get(website)
        
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("ivanpetrov@message.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        
        return welcome_text
        
    def test_registration1(self):
        result_of_registration = self.registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual(result_of_registration, "Congratulations! You have successfully registered!")
        
    def test_registration2(self):
        result_of_registration = self.registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual(result_of_registration, "Congratulations! You have successfully registered!")
        
if __name__ == "__main__":
    unittest.main()

# не забываем оставить пустую строку в конце файла