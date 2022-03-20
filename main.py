import sqlite3

import tweepy as tw
import pandas as pd

consumer_key = '0ONjW2Br8ylQLQ5IfMAQOI42h'
consumer_seceret_key = '7K3OcoXRJYXut1jtGFXyJ7cJ2iGaBSRDWBmeVJ6Cp1iKrfTaZo'
access_token_key = '1480331004028108807-eYYXLeINyx3iovwXXsmugP1YmT4lfM'
access_token_secret = '7Q6K55zVR87SFOl6FfLIAgtyvrm0GZxvDaMtGZyvI01Pd'

#this method connects to the twitter api using the 2-factor authentication method
def get_twitter_api():
    auth = tw.OAuthHandler(consumer_key, consumer_seceret_key)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    return api

#api = get_twitter_api()

#this method searches for tweets related to justin bieber
def tweet_search(search_words, tweet_limit):
    api = get_twitter_api()
    #tw is a module from the twitter api
    tweets = tw.Cursor(api.search_tweets,
                       q=search_words,
                       lang="en").items(tweet_limit)
    return tweets


# filtering tweets related to music
matches = ['music', 'tickets', 'concert', 'Video collaboration']  # the keywords related to music
tweetdates = []
tweetUsers = []
tweetTexts = []
search_words = ["justinbieber","justin bieber", "#justinbieber", "JustinBieber"]

#loop to go through the various tweets
for tweet in tweet_search(search_words, 500):
    if any(x in tweet.text for x in matches):
        tweetdates.append(tweet.created_at)
        tweetUsers.append(tweet.user.screen_name)
        tweetTexts.append(tweet.text)
#creates a dataframe with the following column heads: date, user, tweet
df = pd.DataFrame(list(zip(tweetdates,tweetUsers,tweetTexts)), columns = ['Date','User','Tweet'])

#drop duplicates
df.drop_duplicates()

#check for duplicates in a dataframe
print(df.duplicated(subset=None, keep='first').sum())

#gives the count of all tweets consumed and produces a count of unique counts
print(df.describe())


#Store in a database of choice: sqlite
conn = sqlite3.connect('jb_database')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS bieber (Date date, User text, Tweet text)')
conn.commit()

df.to_sql('bieber', conn, if_exists='replace', index=False)
#extracting the data from database
c.execute('''  
SELECT * FROM bieber
          ''')
for row in c.fetchall():
    print(row)

conn.close()


