from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    website = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(website)

    # Ваш код, который заполняет поля
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    robo_check = browser.find_element(By.ID, "robotCheckbox")
    robo_check.click()
    robo_rule = browser.find_element(By.ID, "robotsRule")
    robo_rule.click()
    
    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла