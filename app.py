import streamlit as st
import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.write("# Real Time Sentiment Analysis")
nltk.download("vader_lexicon")

user_input = st.text_input("Please Input a sentence below:")
if(st.button('Submit')):	
	s = SentimentIntensityAnalyzer()
	score = s.polarity_scores(user_input)
	st.write("Sentiment Analysis:")
	st.write( str(score["pos"]*100)[:4] + "% Positive")
	st.write( str(score["neg"]*100)[:4] + "% Negative")
	st.write( str(score["neu"]*100)[:4] + "% Neutral")

