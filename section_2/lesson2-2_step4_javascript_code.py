from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    #browser.execute_script("alert('Robots at work');")
    #browser.execute_script("document.title='Script executing';")
    #browser.execute_script('document.title="Script executing";')
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла