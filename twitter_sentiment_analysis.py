import tweepy
from textblob import TextBlob
#from textblob_fr import PatternTagger, PatternAnalyzer

#authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#choose the subject of the study
subject_1 = "Infinity"
subject_2 = "War"
#subject_... = "..."

#retrieve Tweets
#options: count = 100 for last 100 tweets
#options: since = "yyyy-mm-dd", until = "yyyy-mm-dd"
tweets = api.search(q=[subject_1, subject_2], count = 100)

#analyse tweets and write in file
for tweet in tweets:
	with open('%s_%s_tweets_sentiment_analysis.csv' % (subject_1, subject_2), 'wb') as tweets_file:
	     tweets_file.write('tweet,sentiment\n')
	     analysis = TextBlob(tweet.text)#, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())    
	     tweets_file.write('%s,%s\n' % (tweet.text.encode('utf8'), analysis.sentiment[0]))
 
#work on your file