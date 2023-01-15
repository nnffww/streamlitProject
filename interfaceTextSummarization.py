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

#Set window background color
window.config(background = "white")
    
if choice == 'News Article': 
  category = ["Business","Entertaiment","Politics","Sport", "Technology"]
  option = st.selectbox("Select News Article", category)
    
***
  if category == 'Business':
    st.button("Ad sales boost Time Warner profit")
    if st.button("Ad sales boost Time Warner profit")
        url = ('https://raw.githubusercontent.com/faraawaheeda/streamlitProject/main/business/001.txt')
        for line in urllib.request.urlopen(url): 
            st.write(line.decode('utf-8'))
***
  
if choice == 'Summarize': 
   st.subheader("EXTRACTIVE TEXT SUMMARIZER")
   agree = st.checkbox('Show sentence')
   raw_text = st.text_area("Original Content","Enter text here")
   uploaded_file = st.file_uploader("Choose a file")
   if uploaded_file is not None:
      # To read file as bytes:
      bytes_data = uploaded_file.getvalue()
      st.write(bytes_data)
      # To convert to a string based IO:
      stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
      st.write(stringio)
      # To read file as string:
      string_data = stringio.read()
      st.write(string_data)
      # Can be used wherever a "file-like" object is accepted:
      dataframe = pd.read_csv(uploaded_file)
      st.write(dataframe)
   if st.button("Summarize"):
      st.write(raw_text)
      st.button("Copy text")
      st.write("Words:")
  
