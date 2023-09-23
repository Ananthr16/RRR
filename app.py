#importing the libraries
import streamlit as st
from ultralytics import YOLO
import openai
from PIL import Image
import time
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

#setting the page
st.set_page_config(initial_sidebar_state = 'collapsed')
selected = option_menu(
            menu_title=None,  # required
            options=["Home", "AI Model", "Segregation"],  # required
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
if selected == "Home":
	switch_page("app")
if selected == 'AI Model':
	switch_page('AI Model')
if selected == 'Segregation':
	switch_page('Segregation')
st.title('Reduce, Recycle, Reuse')
st.subheader('''The RRR Web Application uses a 2 step ML Model backed up with multiple data sets as well as a customized data set to identify the object and the material after which it provides ways to reduce, reuse, and recycle the obejct.  ''') 
