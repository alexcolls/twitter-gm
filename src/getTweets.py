from src.chromeDriver import driver, by

tweetObj = {
    'id': 'selenium class',
    'type': 'tweet',  # tweet type - line 27 to 44
    'user': str,
    'name': str,
    'tweet': str,  # text content
    'likes': int,
    'retweets': int,
    'comments': int,
    'views': int,
    'promoted': bool,
}


def get_tweets(_driver=driver, _print=False, _ln=70):
    tweetsRaw = _driver.find_elements(by=by.TAG_NAME, value='article')
    tweets = []
    for tweetRaw in tweetsRaw:
        try:
            text = tweetRaw.text
            textArr = text.split('\n')
            type_ = 'tweet'
            i = 0
            if (text[:_ln].__contains__('liked')):
                i += 1
                type_ = 'liked'
            elif (text[:_ln].__contains__('follow')):
                i += 1
                type_ = 'follow'
            elif (text[:_ln].__contains__('replied')):
                i += 1
                type_ = 'replied'
            elif (text[:_ln].__contains__('Retweeted')):
                i += 1
                type_ = 'retweet'
            elif (text[:_ln].__contains__('See more')):
                i += 1
                type_ = 'see-more'
            elif (text[:_ln].__contains__('Replying to')):
                i += 2
                type_ = 'replying'
            j = 0
            if (text[:_ln].__contains__('· ')):
                j += 4
            twObj = {
                'id': tweetRaw,
                'type': type_,
                'name': textArr[0+i],
                'user': textArr[1+i],
                'tweet': textArr[4+i+j],
                'comments': textArr[5+i+j],
                'retweets': textArr[6+i+j],
                'likes': textArr[7+i+j],
                'views': textArr[8+i+j],
                'promoted': True if text[-20].__contains__('Promoted') else False,
            }
            tweets.append(twObj)
            if (_print):
                print('\n', twObj, '\n')
        except:
            continue

    return tweets


if __name__ == '__main__':
    tweets = get_tweets()
    for tweet in tweets:
        print('\n', tweet)
