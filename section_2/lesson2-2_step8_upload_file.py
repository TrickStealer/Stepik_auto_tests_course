from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    webpage = "http://suninjuly.github.io/file_input.html"
    browser.get(webpage)
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("IvanPetrov@gm.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')
    input_file = browser.find_element(By.ID, "file")
    input_file.send_keys(file_path)
    
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла