from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    webpage = "http://suninjuly.github.io/execute_script.html"
    browser.get(webpage)
    
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    
    browser.execute_script("window.scrollBy(0, 100);")
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    robo_check = browser.find_element(By.ID, "robotCheckbox")
    robo_check.click()
    robo_rule = browser.find_element(By.ID, "robotsRule")
    robo_rule.click()
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла