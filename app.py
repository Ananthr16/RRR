#importing the libraries
import streamlit as st
from ultralytics import YOLO
import openai
from PIL import Image
import time
from streamlit_extras.switch_page_button import switch_page

#setting the page
st.set_page_config(initial_sidebar_state = 'collapsed',layout = 'wide')
col = st.columns(9)
with col[0]:
	if st.button("AI Model"):
		switch_page('AI Model')
with col[2]:
	if st.button("Plastic(recyclable)"):
		switch_page('Plastic(recyclable)')

with col[4]:
	if st.button("Plastic non recyclable"):
		switch_page('Plastic non recyclable')
with col[6]:
	if st.button("Paper\Cardboard"):
		switch_page('Paper\Cardboard')
with col[8]:
	if st.button("E-Waste"):
		switch_page('E-Waste')





st.title('Reduce, Recycle, Reuse')
st.subheader('''The RRR Web Application uses a 2 step ML Model backed up with multiple data sets as well as a customized data set to identify the object and the material after which it provides ways to reduce, reuse, and recycle the obejct.  ''') 


