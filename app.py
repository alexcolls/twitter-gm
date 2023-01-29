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
        print(tweets)
        # for tweet in tweets:
        #     print(tweet.tweet)
        #     ans = create_tweet(tweet.tweet)
        #     print(ans)
        run = False
        break
    except:
        sleep(5)
        driver.get('https://www.twitter.com/home')
        continue
