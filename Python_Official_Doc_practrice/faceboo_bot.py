# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys

 
# usr=input('enter email')
# pwd=input('enter password')
 
# driver = webdriver.Chrome()
# driver.get('https://mbasic.facebook.com/')
# print ("Opened facebook")
# sleep(1)
 
# username_box = driver.find_element_by_name('email')
# username_box.send_keys(usr)
# print ("Email Id entered")
# sleep(1)
 
# password_box = driver.find_element_by_name('pass')
# password_box.send_keys(pwd)
# print ("Password entered")
 
# login_box = driver.find_element_by_name('login')
# login_box.click()

# onetap_btn = driver.find_element_by_xpath("//input[@type='submit']")
# onetap_btn.click()

# query = "Hasan Mahmud Shojib"

# search_box = search_box = driver.find_element_by_name('query')
# search_box.send_keys(query)

# search_btn = driver.find_element_by_xpath("//input[@type='value']")
# search_btn.send_keys('Search')
# search_btn.click()

# sleep(1)


# print ("Done")
# input('Press anything to quit')
# driver.quit()
# print("Finished")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser=webdriver.Chrome()
try:
        browser.get("https://en.wikipedia.org")
        print(browser.title)
        input=browser.find_element_by_id("searchInput")
        input.send_keys("Python")
        input.send_keys(Keys.ENTER)
        wait=WebDriverWait(browser,10)
        wait.until(EC.presence_of_element_located((By.ID,"content")))
        print(browser.title)
        #print(browser.get_cookies())
        #print(browser.page_source)
        time.sleep(10)
finally:
        browser.close()