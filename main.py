import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("https://www.github.com/")
driver.set_window_size(1200, 800)

# Home page
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')
login_button.click()

# Login page
email = str(input("Email: "))
pwd = str(input("MDP: "))

email_field = driver.find_element(By.XPATH, '/html/body/div[3]/main/div/div[4]/form/input[2]')
password_field = driver.find_element(By.XPATH, '/html/body/div[3]/main/div/div[4]/form/div/input[1]')

for i in email:
    email_field.send_keys(i)
    
for i in pwd:
    password_field.send_keys(i)

sign_in_button = driver.find_element(By.XPATH, '/html/body/div[3]/main/div/div[4]/form/div/input[12]')
sign_in_button.click()

time.sleep(5)

try:
    print('here')
    driver.find_element(By.XPATH, '/html/body/div[3]/main/div/div[2]')
    print('Veuillez vérifier vos coordonnées')
except:
    print('c fait!')
    
input("Press the <ENTER> key to continue...")