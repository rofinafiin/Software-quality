from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get('https://siakad.ulbi.ac.id')

sleep(1)

username_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")


login_button = driver.find_element(By.CLASS_NAME, "btn-login")


username_input.send_keys("1214017")
password_input.send_keys("rofiganteng123")


login_button.click()

okbutton = driver.find_element(By.CLASS_NAME, "btn-login")
okbutton.click()

element = driver.find_element(By.ID, "link-siakad")
element.click()


# Locate the div element
cont = driver.find_element(By.CLASS_NAME, "role_box")

# Get the onclick attribute value
onclick_value = cont.get_attribute("onclick")

# Print or use the onclick value as needed
print(onclick_value)
sleep(9999999)


