from time import sleep
from src.login import log_in
from src.getTweets import get_tweets
from src.createTweet import create_tweet
from src.chromeDriver import driver
run = True
log_in()
sleep(2)
i = 0
while run:
    print(i)
    try:
        i += 1
        driver.refresh()
        sleep(5)
        tweets = get_tweets()
        prompts = []
        for tweet in tweets:
            tweet.ans = create_tweet(tweet.tweet)
        print(tweets)
        break
    except:
        sleep(5)
        driver.get('https://www.twitter.com/home')
        continue
