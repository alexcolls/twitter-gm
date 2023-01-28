from src.chromeDriver import driver, by

tweetObj = {
    'user': str,
    'name': str,
    'tweet': str,
    'likes': int,
    'retweets': int,
    'comments': int,
    'views': int,
    'promoted': bool,
}


def get_tweets():
    tweetsRaw = driver.find_elements(by=by.TAG_NAME, value='article')
    tweets = []
    for tweetRaw in tweetsRaw:
        text = tweetRaw.text
        print(text)
        print(type(text))
        twObj = {
            'id': tweetRaw,
            'user': str,
            'name': str,
            'tweet': str,
            'likes': int,
            'retweets': int,
            'comments': int,
            'views': int,
            'promoted': bool,
        }
        break
