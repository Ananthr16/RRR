#importing the libraries
import streamlit as st
from ultralytics import YOLO
import openai
from PIL import Image
import time
from streamlit_extras.switch_page_button import switch_page

#setting the page
st.set_page_config(initial_sidebar_state = 'collapsed',layout = 'wide')

st.title('Reduce, Recycle, Reuse')
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
	
col = st.columns(9)
with col[0]:
	if st.button("Plastic recyclable" , key = count):
		switch_page('Plastic(recyclable)')
		count += 1

with col[4]:
	if st.button("Plastic non recyclable"):
		switch_page('Plastic non recyclable')

with col[8]:
	if st.button("E-Waste"):
		switch_page('E-Waste')


