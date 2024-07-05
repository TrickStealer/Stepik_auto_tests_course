from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    webpage = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(webpage)
    browser.implicitly_wait(5)
    
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    book_button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    book_button.click()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    button = browser.find_element(By.ID, "solve")
    button.click()

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла