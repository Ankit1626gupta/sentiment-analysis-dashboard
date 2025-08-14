from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import db
def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer() #object banaa hai SentimentIntensityAnalyzer 
    score = analyzer.polarity_scores(text) #har character ka score dega
    compound = score['compound'] # phir sab score ka avg nikal kr compound me store krdo 
    
    
    if compound >= 0.05:
            return "Positive😊"
    elif compound <= -0.05:
        return "Negative😢"
    else:
        return "Neutral😐"  