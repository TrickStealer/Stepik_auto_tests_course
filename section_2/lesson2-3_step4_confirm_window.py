from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    webpage = "http://suninjuly.github.io/alert_accept.html"
    browser.get(webpage)
    
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    time.sleep(1)
    
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла