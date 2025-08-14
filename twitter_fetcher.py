import tweepy as tw
import db
import pandas as pd 
import streamlit as st
#import time
bearer_token = "AAAAAAAAAAAAAAAAAAAAANBd2QEAAAAAeVDzx7WkWs94j02LFztVRhvPYvg%3DyoK9TMuuO13LvCcXj4zgLV5SROluqz1IINXFa5o8GSBQJpLKCq"
client = tw.Client(bearer_token=bearer_token)

def fetch(query, count=10):
    tweets = []
    tweet_db=[]
    try:
        responses = client.search_recent_tweets(
        query= query + " lang:en",
        max_results=count,
        tweet_fields=["lang"]
    )
        if responses.data:
            for tweet in responses.data:
                 if tweet.lang == "en":
                   tweets.append(tweet.text)
    except tw.TooManyRequests:
        st.subheader("Due To TooManyRequests error These Are Data From Database")
        df=db.wil(query)    
        cd=pd.DataFrame(df,columns=["TEXT","SENTIMENT","TIMESTAMP"])
        st.dataframe(cd)
    return tweets
#print(fetch("AI", 10))
#time.sleep(10)