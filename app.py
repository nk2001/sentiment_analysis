import streamlit as st
import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.write("# Real Time Sentiment Analysis")

user_input = st.text_input("Please Input a sentence below:")
if(st.button('Submit')):
	nltk.download("vader_lexicon")
	s = SentimentIntensityAnalyzer()
	score = s.polarity_scores(user_input)
	st.write("The sentence is analyzed as follows")
	st.write( str(score["pos"]*100) + "% Positive")
	st.write( str(score["neg"]*100) + "% Negative")
	st.write( str(score["neu"]*100) + "% Neutral")

