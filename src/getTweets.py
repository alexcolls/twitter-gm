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
        textArr = text.split('\n')
        twObj = {
            'id': tweetRaw,
            'user': textArr[1],
            'name': textArr[0],
            'tweet': textArr[4],
            'comments': textArr[5],
            'retweets': textArr[6],
            'likes': textArr[7],
            'views': textArr[8],
            'promoted': True if text.__contains__('Promoted') else False,
        }
        print('\n', twObj, '\n')
        tweets.append(twObj)
