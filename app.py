import streamlit as st
from transformers import pipeline
from dotenv import load_dotenv
import os
load_dotenv()

model_path=os.getenv('MODEL')
model = pipeline(task='sentiment-analysis', model=model_path)

st.title("Sentiment Analysis App")

user_input = st.text_input("Enter a sentence for sentiment analysis:")

if st.button("Analyze Sentiment"):
    if user_input:
     
        result = model(user_input)
        sentiment = result[0]['label']
        score = result[0]['score']
        
        st.write(f"Sentiment: {sentiment} (Confidence: {score:.2f})")
    else:
        st.write("Please enter a sentence to analyze.")

