from time import sleep
from src.login import log_in
from src.getTweets import get_tweets
from src.chromeDriver import driver
run = True
log_in()
sleep(2)
while run:
    try:
        driver.refresh()
        sleep(5)
        tweets = get_tweets()
        print(tweets)
        sleep(25)
    except:
        sleep(5)
        driver.get('https://www.twitter.com/home')
        continue
