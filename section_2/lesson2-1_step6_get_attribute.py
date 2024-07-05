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

    #people_radio = browser.find_element(By.ID, "peopleRule")
    #people_checked = people_radio.get_attribute("checked")
    #print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"
    #assert people_checked == "true", "People radio is not selected by default"
    
    #robots_radio = browser.find_element(By.ID, "robotsRule")
    #robots_checked = robots_radio.get_attribute("checked")
    #print("value of robots radio: ", robots_checked)
    #assert robots_checked is not None, "Robot radio is not selected by default"
    #assert robots_checked == "true", "People radio is not selected by default"
    
    button = browser.find_element(By.CLASS_NAME, "btn")
    button_disabled = button.get_attribute("disabled")
    print("Is button disabled: ", button_disabled)
    print("Waiting")
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("Is button disabled: ", button_disabled)
    #assert robots_checked is not None, "Robot radio is not selected by default"
    #assert button_disabled == "true", "People radio is not selected by default"


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла