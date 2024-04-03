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
time.sleep(5)

element = driver.find_element(By.XPATH, "//a[text()='Request Loan']")
element.click()
time.sleep(5)

driver.find_element(By.ID, "amount").send_keys('100')
driver.find_element(By.ID, "downPayment").send_keys('50')
time.sleep(5)
driver.find_element(By.XPATH, '//input[@value="Apply Now"]').click()


