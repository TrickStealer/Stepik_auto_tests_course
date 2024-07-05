from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

try:
    browser = webdriver.Chrome()
    webpage = "http://suninjuly.github.io/wait1.html"
    browser.get(webpage)
    browser.implicitly_wait(5)
    
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла