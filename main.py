import tweepy, time

CONSUMER_KEY = 'xxx' 
CONSUMER_SECRET = 'xxx' 
ACCESS_TOKEN = 'xxx' 
ACCESS_SECRET = 'xxx' 

#authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

filename=open('data.txt')
fname=filename.readlines()
filename.close()

for line in fname:
    try:
        api.update_status(line)
        print("Tweeting!")
    except tweepy.TweepError as err:
        print(err)
    time.sleep(45) #Tweet every 1 minute
print("Done!")
