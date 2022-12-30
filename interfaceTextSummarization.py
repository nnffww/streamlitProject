import streamlit as st  
import pandas as pd
import numpy as np
import io
import requests
import urllib.request
import urllib
from urllib.request import urlopen
import urllib3

st.set_page_config(page_title="Extractive Text Summarization", page_icon=":tada:", layout="wide")
st.markdown("<h1 style='text-align: center; color: white;'>EXTRACTIVE BASED TEXT SUMMARIZATION USING SENTIMENT ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<hr size='5' width='100%;'>", unsafe_allow_html=True)
activities = ["About Us","News Article","Summarize","Statistic"]
choice = st.sidebar.selectbox("Select Activity", activities)
    
if choice == 'News Article': 
  category = ["A","B","C","D"]
  option = st.selectbox("Select News Article", category)
  
  if category == 'A':
    st.button("Ad sales boost Time Warner profit")
    if st.button("Ad sales boost Time Warner profit")
        url = ('https://raw.githubusercontent.com/faraawaheeda/streamlitProject/main/business/001.txt')
        for line in urllib.request.urlopen(url): 
            st.write(line.decode('utf-8'))
  
  
