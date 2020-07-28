import tweepy_test

#tweepy auth function
def tweepy_auth(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

#tweepy retweet likes function
def retweet_favorites(api, username):
    for tweet in api.favorites(username):
        try:
            api.retweet(tweet.id)
        except tweepy.TweepError as e:
            print(e)
    return print("Done!")