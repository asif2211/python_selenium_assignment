import time
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.aa.com/aa/reservation/flightCheckInViewReservationsAccess.do')
print(driver.title)
time.sleep(10)

element = driver.find_element_by_id("findReservationForm.firstName").send_keys('abc')
if element:
    print('this is exist')

