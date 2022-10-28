# import libraries
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
from time import sleep
import numpy as np

import keypair

user = keypair.user
pasw = keypair.pasw

# open chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.twitter.com/i/flow/login')

user_in = driver.find_element(by=By.TAG_NAME, value='input')
user_in.send_keys(user)
user_in.send_keys(Keys.ENTER)

pasw_in = driver.find_element(by=By.NAME, value='password')
pasw_in.send_keys(pasw)
pasw_in.send_keys(Keys.ENTER)

driver.refresh()


tweets = driver.find_elements(by=By.TAG_NAME, value='article')
test = tweets[0].find_elements(by=By.TAG_NAME, value='svg')[3].click()

reply_in = driver.find_element(by=By.CLASS_NAME, value='public-DraftStyleDefault-block')
reply_in.send_keys ('gm')

divs = driver.find_elements(by=By.TAG_NAME, value='div')

for div in divs:
  div.submit()

driver.send_keys('test')
for tweet in tweets:
  reply_in = tweet.find_elements(by=By.TAG_NAME, value='svg')[3].click()


like = driver.find_element(by=By.ID, value='id__rjm2ynw6cy')

like
like = driver.find_element(by=By.CLASS_NAME, value='r-xoduu5')


like.click()
for tweet in tweets:
  driver.find_element(by=By.CLASS_NAME, value='r-xoduu5')
  sleep(100)
  tweet.click()


