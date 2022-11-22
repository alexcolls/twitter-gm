from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randint

import keypair as keypair

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def log_in ( user=keypair.user, pasw=keypair.pasw ):
  driver.get('https://www.twitter.com/i/flow/login')
  sleep(2)
  user_in = driver.find_element(by=By.TAG_NAME, value='input')
  user_in.send_keys(user)
  user_in.send_keys(Keys.ENTER)
  sleep(2)
  pasw_in = driver.find_element(by=By.NAME, value='password')
  pasw_in.send_keys(pasw)
  pasw_in.send_keys(Keys.ENTER)

log_in()
sleep(3)

messages = [
  'Gm',
  'Gmgmgmgm',
  'Gm ❤️',
  'Hi darling',
  'Gm 👽',
  'Gmmmm',
  'whatsup',
  'congrats',
  'hello',
  'cool',
  '❤️',
  'hey',
  'I love you',
  'God loves you',
  'respect',
  'positivity',
  'productivity',
  'have a nice day ❤️',
  '❤️❤️❤️'
  'be happy',
  'hi dear',
  'lfgggg',
  'LFG 🚀',
  '🚀',
  '🚀🚀🚀'
]

while True:
  try: 
    driver.refresh()
    sleep(5)
    tweets = driver.find_elements(by=By.TAG_NAME, value='article')
    tweet = tweets[3]
    svgs = tweet.find_elements(by=By.TAG_NAME, value='svg')
    svgs[3].click() # like
    svgs[1].click() # comment
    sleep(5)
    reply_in = driver.find_element(by=By.CLASS_NAME, value='public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
    i = randint(0, len(messages)-1)
    print('\n', i, '\n', messages[i])
    sleep(3)
    reply_in.send_keys (messages[i])
    sleep(2)
    reply_in.send_keys(Keys.ENTER)
    reply = driver.find_elements(by=By.TAG_NAME, value='span')
    for r in reply:
      if r.text == 'Reply':
        r.click()
        break
      elif r.text == 'Unsent Tweet':
        break
    sleep(8)
  except:
    sleep(2)
    driver.get('https://www.twitter.com/home')
    continue


# tweets = driver.find_elements(by=By.TAG_NAME, value='article')

# for tweet in tweets:
#   mess = tweet.find_elements(by=By.TAG_NAME, value='span')[4].text
#   if mess == 'See more':
#     mess = tweet.find_elements(by=By.TAG_NAME, value='span')[6].text
#   print(mess)


# tweet.click()

# for tweet in tweets:

#   try: 
#     svgs = tweet.find_elements(by=By.TAG_NAME, value='svg')
#     svgs[1].click()#like
#     svgs[5].click()
#   except:
#     svg
#   tweet.find_elements(by=By.TAG_NAME, value='svg')[3].click() # like click
#   sleep(1)
#   tweet.find_elements(by=By.TAG_NAME, value='svg')[1].click() # comment click
#   sleep(1)
#   reply_in = driver.find_element(by=By.CLASS_NAME, value='public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
#   i = randint(0, len(messages)-1)
#   reply_in.send_keys (messages[i])
#   reply = driver.find_elements(by=By.TAG_NAME, value='span')
#   for r in reply:
#     if r.text == 'Reply':
#       r.click()
#       break
#   sleep(1)
