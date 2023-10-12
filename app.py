#importing the libraries
import streamlit as st
from ultralytics import YOLO
import openai
from PIL import Image
import time
from streamlit_extras.switch_page_button import switch_page
import json 
import requests 
from streamlit_lottie import st_lottie



def load_lottieurl(url: str):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json ()

lottie_hello = load_lottieurl("https://lottie.host/ddedf6f1-8fdf-412b-9e40-76237fa2df77/W6X4B23V5f.json")

#setting the page
st.set_page_config(initial_sidebar_state = 'collapsed',layout = 'wide')
st.markdown(
         """
         <style>
         .stApp {
             background-image: linear-gradient(to right,sky blue, purple);
         }
         </style>
         """,
         unsafe_allow_html=True)
st_lottie(lottie_hello,key='hello')

st.title('R R R')
st.subheader('''RRR: Reduce, Recycle, Reuse 
RRR is a Web-based App which helps you decide what you can do with any item or material in order to dispose of it sustainability, and with least harm to the environment. 
 \n It uses a 2 step ML Model backed up with multiple data sets as well as a customized data set. 
 \n This helps to identify the object/material using your camera, after which it provides ways to reduce, reuse, and recycle it. 
\n Use it to lead a healthy and less wasteful life. And protect our earth - the only home we have. ''') 
count = 0
colum = st.columns(1)
with colum[0]:
	if st.button("AI Model"):
		switch_page('AI Model')
	


st.subheader('''Waste can be categorised as follows :''')




col = st.columns(9)
with col[0]:
	if st.button("Biodegradable" , key = count):
		switch_page('Biodegradable')
		count += 1

with col[4]:
	if st.button("Non-Biodegradable"):
		switch_page('Non-Biodegradable')

with col[8]:
	if st.button("Hazardous Waste"):
		switch_page('Hazardous')


