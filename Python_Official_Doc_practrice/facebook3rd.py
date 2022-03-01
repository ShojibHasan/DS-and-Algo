from selenium import webdriver
from getpass import getpass
from time import sleep,time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

usr = 'mahfujul.hasan@bjitgroup.com'
pwd = 'shojib74462'
search= "Hasan Mahmud Shojib"

driver = webdriver.Chrome()
driver.get('https://erp.bjitgroup.com/web')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_name('login')
login_btn.submit()
sleep(2)

# search_box = driver.find_element_by_xpath("//input[@type='search']")


# search_box.send_keys("Hasan Mahmud Shojib")
# search_box.send_keys(Keys.ENTER)


sleep(5)