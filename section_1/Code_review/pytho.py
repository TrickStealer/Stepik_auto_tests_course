from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, "div.first_class input")
    name.send_keys("Vova")
    surname = browser.find_element(By.CSS_SELECTOR, "div.second_class input")
    surname.send_keys("Vova")
    email = browser.find_element(By.CSS_SELECTOR, "div.third_class input")
    email.send_keys("Vova1@ma.ma")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()