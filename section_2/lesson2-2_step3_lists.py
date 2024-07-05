from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    website = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(website)
    
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    print("num1 = ", num1, ", num2 = ", num2)
    
    result = num1 + num2
    result_selector = "[value='" + str(result) + "']"
    print("result: ", result)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла