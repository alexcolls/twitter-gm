# import libraries
import functions as tw

blacklist = []

# open chrome driver





tw.log_in()

tw.driver.refresh()

tweets = tw.driver.find_elements(by=tw.By.TAG_NAME, value='article')
tw.sleep(2)


for tweet in tweets:
  user = tweet.find_elements(by=tw.By.TAG_NAME, value='span')[0].text
  if user in blacklist:
    continue

  mess = tweet.find_elements(by=By.TAG_NAME, value='span')[4].text
  print(mess)
  
  sleep(1)
  if 'gm' in mess:   
    tweets[0].find_elements(by=By.TAG_NAME, value='svg')[5].click() # like click
    sleep(1)
    tweets[0].find_elements(by=By.TAG_NAME, value='svg')[3].click() # comment click
    sleep(1)
    reply_in = driver.find_element(by=By.CLASS_NAME, value='public-DraftStyleDefault-block')
    reply_in.send_keys ('gm')
    reply_in.send_keys (Keys.ENTER)
  else:
    continue

  input('continue?')









like = driver.find_element(by=By.ID, value='id__rjm2ynw6cy')

like
like = driver.find_element(by=By.CLASS_NAME, value='r-xoduu5')


like.click()
for tweet in tweets:
  driver.find_element(by=By.CLASS_NAME, value='r-xoduu5')
  sleep(100)
  tweet.click()


