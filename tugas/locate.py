from selenium import webdriver
from selenium.webdriver.common.by import By
import time



options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
driver.find_element(By.CLASS_NAME, "gLFyf").send_keys('python')
time.sleep(5)

button = driver.find_element(By.CLASS_NAME, 'gNO89b')
button.click()


link= driver.find_element(By.LINK_TEXT, "https://www.python.org/")

link.click()