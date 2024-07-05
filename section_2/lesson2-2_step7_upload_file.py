from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла