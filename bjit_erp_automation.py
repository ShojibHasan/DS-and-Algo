

# 1. Download chrome driver from https://sites.google.com/chromium.org/driver/

# 2. Run the python file



import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"/home/shojibhasan/Documents/DS-and-Algo/chromedriver_linux64/chromedriver")

# open login webpage
driver.get("http://localhost:8088/web/login")

my_username = "admin@bjitgroup.com"
my_password = "admin"

# access login username input
username_input_box = driver.find_element(By.NAME, 'login')

# access login password input
password_input_box = driver.find_element(By.NAME, 'password')

# access login button
sign_up_button = driver.find_element(By.TAG_NAME,"button")

# clear the placeholders data
username_input_box.clear()
password_input_box.clear()

# fill login credentials
username_input_box.send_keys(my_username)
# time.sleep(1)
password_input_box.send_keys(my_password)
time.sleep(5)
# hit the login button

sign_up_button.click()

time.sleep(1)

driver.get("http://localhost:8088/web#menu_id=408&action=564")

time.sleep(2)

punch_button = driver.find_element(By.CSS_SELECTOR,".fa.fa-sign-in.btn-primary.o_hr_attendance_punch.o_hr_attendance_sign_in_out_icon")
print("I'm after punch button: ",punch_button)
punch_button.click()
print("punch button click: ")
# time.sleep(2)
# driver.get("https://erp.bjitgroup.com/web#view_type=list&model=hr.attendance&menu_id=316")

# driver.get("http://localhost:8088/web#action=449")

time.sleep(3)

# close the driver
# driver.close()
