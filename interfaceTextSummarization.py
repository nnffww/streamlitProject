import streamlit as st  
import pandas as pd
import numpy as np

st.set_page_config(page_title="Extractive Text Summarization", page_icon=":tada:", layout="wide")
st.markdown("<h1 style='text-align: center; color: white;'>EXTRACTIVE BASED TEXT SUMMARIZATION USING SENTIMENT ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<hr size='5' width='100%;'>", unsafe_allow_html=True)
activities = ["Introduction","News Article","Summarize","Statistic"]
choice = st.sidebar.selectbox("Select Activity", activities)

if choice == 'News Article': 
  category = ["A","B","C","D"]
  option = st.selectbox("Select News Article", category)
  
