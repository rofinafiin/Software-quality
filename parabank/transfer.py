from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://parabank.parasoft.com/parabank/index.htm")
time.sleep(10)

driver.find_element(By.NAME, "username").send_keys('python')
driver.find_element(By.NAME, "password").send_keys('python')


driver.find_element(By.XPATH, '//input[@value="Log In"]').click()


element = driver.find_element(By.XPATH, "//a[text()='Transfer Funds']")
element.click()
time.sleep(5)

driver.find_element(By.ID, "amount").send_keys('1')
time.sleep(5)
driver.find_element(By.XPATH, '//input[@value="Transfer"]').click()

