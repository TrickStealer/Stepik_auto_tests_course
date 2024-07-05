from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://www.degreesymbol.net/"
browser = webdriver.Chrome()
browser.get(link)
# text_link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
text_link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
text_link.click()

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()