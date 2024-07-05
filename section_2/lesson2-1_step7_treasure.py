from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    website = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(website)
    
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    
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