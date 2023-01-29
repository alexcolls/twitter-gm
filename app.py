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
    i += 1
    print('\nRun: ', i)
    try:
        driver.refresh()
        sleep(5)
        tweets = get_tweets(True)
        # print(tweets)
        j = 0
        for tw in tweets:
            j += 1
            print('\n\n', 'Tweet: ', j)
            print('\n', tw)
            ans = create_tweet([tw['tweet']])
            print('\n', ans)
            sleep(10)
        sleep(20)
    except:
        sleep(60)
        print('ERROR at Run and Tweet: ', i, j)
        driver.get('https://www.twitter.com/home')
        continue
