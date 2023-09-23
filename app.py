#importing the libraries
import streamlit as st
from ultralytics import YOLO
import openai
from PIL import Image
import time
from streamlit_extras.switch_page_button import switch_page

#setting the page
st.set_page_config(initial_sidebar_state = 'collapsed')
st.title('Reduce, Recycle, Reuse')
st.subheader('''The RRR Web Application uses a 2 step ML Model backed up with multiple data sets as well as a customized data set to identify the object and the material after which it provides ways to reduce, reuse, and recycle the obejct.  ''') 

col = st.columns(4)
with col[0]:
	if st.button("AI Model"):
		switch_page('AI Model')
with col[1]:
	if st.button("Plastic(recyclable)"):
		switch_page('Plastic(recyclable)')
with col[2]:
	if st.button("")
