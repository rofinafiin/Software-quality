from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://parabank.parasoft.com/")
time.sleep(2)
element = driver.find_element(By.XPATH, "//a[text()='Register']")
element.click()

time.sleep(5)

driver.find_element(By.NAME, "customer.firstName").send_keys('python')
time.sleep(2)
driver.find_element(By.NAME, "customer.lastName").send_keys('python')
time.sleep(2)
driver.find_element(By.NAME, "customer.address.street").send_keys('st paint')
time.sleep(2)
driver.find_element(By.NAME, "customer.address.city").send_keys('paint')
time.sleep(2)
driver.find_element(By.NAME, "customer.address.state").send_keys('state')
time.sleep(2)
driver.find_element(By.NAME, "customer.address.zipCode").send_keys('1111')
time.sleep(2)
driver.find_element(By.NAME, "customer.phoneNumber").send_keys('00089202')
time.sleep(2)
driver.find_element(By.NAME, "customer.ssn").send_keys('1')
time.sleep(2)
driver.find_element(By.NAME, "customer.username").send_keys('steam')
time.sleep(2)
driver.find_element(By.NAME, "customer.password").send_keys('python')
time.sleep(2)
driver.find_element(By.NAME, "repeatedPassword").send_keys('python')
time.sleep(2)


driver.find_element(By.XPATH, '//input[@value="Register"]').click()
time.sleep(10)
driver.quit()