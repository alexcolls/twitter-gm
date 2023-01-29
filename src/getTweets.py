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
        i = 0
        first = 50  # characters of tweet
        if (text[:first].__contains__('liked')):
            i += 1
        elif (text[:first].__contains__('follow')):
            i += 1
        elif (text[:first].__contains__('Retweeted')):
            i += 1
        elif (text[:first].__contains__('replied')):
            i += 1
        elif (text[:first].__contains__('See more')):
            i += 1
        twObj = {
            'id': tweetRaw,
            'name': textArr[0+i],
            'user': textArr[1+i],
            'tweet': textArr[4+i],
            'comments': textArr[5+i],
            'retweets': textArr[6+i],
            'likes': textArr[7+i],
            'views': textArr[8+i],
            'promoted': True if text[-20].__contains__('Promoted') else False,
        }
        tweets.append(twObj)
        print('\n', twObj, '\n')
    return tweets
