from secrets import *
import tweepy

def get_id(text):
    return text.split('/')[-1].split('?')[0]

def api_init():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api

def get_url(api, twid):
    try:
        twid = int(twid)
    except:
        return ('Error: The tweet url is not valid, try /help for more information')

    try:
        tweet = api.get_status(twid)
    except:
        return('Error: Invalid tweet, is your link correct?')

    try:
        variants = tweet.extended_entities['media'][0]['video_info']['variants'][::-1]
    except:
        return('Error: This tweet has no video')

    flag = True
    # getting the highest bitrate mp4
    for v in variants:
        if (v['content_type'] == 'video/mp4'):
            if(flag):
                best = v
                flag = False
            elif(v['bitrate'] > best['bitrate']):
                best = v
    try:
        return best['url']
    except:
        return('Error: Are you sure this is a video tweet?')
