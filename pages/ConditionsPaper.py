import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Paper')

st.title('Conditions to hand over Paper waste to commercials recyclers')

st.markdown(''' Segregate clean and dry paper and cardboard at source, bring to RRC ''')
