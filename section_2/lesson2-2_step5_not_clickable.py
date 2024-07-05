from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    webpage = "https://SunInJuly.github.io/execute_script.html"
    browser.get(webpage)
    
    browser.execute_script("window.scrollBy(0, 100);")
    button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла