from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://en.wikipedia.org/wiki/Car")


elems = driver.find_element(By.CLASS_NAME, "mw-page-container-inner")
print(elems.text)
time.sleep(6)
driver.close()
