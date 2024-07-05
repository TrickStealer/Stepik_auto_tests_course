from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

try:
    browser = webdriver.Chrome()
    webpage = "http://suninjuly.github.io/cats.html"
    browser.get(webpage)
    browser.implicitly_wait(5)
    
    button = browser.find_element(By.ID, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла