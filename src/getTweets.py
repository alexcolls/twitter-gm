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


def get_tweets(_print=False, _driver=driver, _ln=70):
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
            elif (text[:_ln].__contains__('new replies')):
                i += 1
                type_ = 'new-replies'
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
            k = 0
            for idx in range(4+i+j, len(textArr)):
                try:
                    if (int(textArr[int(idx)]) >= 0):
                        break
                    else:
                        k += 1
                except:
                    k += 1
            twObj = {
                'id': tweetRaw,
                'type': type_,
                'name': textArr[0+i],
                'user': textArr[1+i],
                'tweet': ' '.join(textArr[4+i+j: 4+i+j+k]),
                'comments': textArr[5+i+j+k],
                'retweets': textArr[6+i+j+k],
                'likes': textArr[7+i+j+k],
                'views': textArr[8+i+j+k],
                'promoted': True if text[-30].__contains__('Promoted') else False,
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
