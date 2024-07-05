from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    webpage = "http://suninjuly.github.io/wait2.html"
    browser.get(webpage)
    browser.implicitly_wait(5)
    
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла