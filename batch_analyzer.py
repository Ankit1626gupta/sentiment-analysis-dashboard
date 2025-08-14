import db
import analyzer
import twitter_fetcher as tf
def analyze_and_store(query,count=10):
     tweets=tf.fetch(query,count)
     for tweet in tweets:
        sentiment = analyzer.get_sentiment(tweet)
        db.insert_data(tweet, sentiment)
    