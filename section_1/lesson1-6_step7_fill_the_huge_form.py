from selenium import webdriver
from selenium.webdriver.common.by import By
import time

website = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(website)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла