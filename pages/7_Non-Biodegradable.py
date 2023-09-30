import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('app')

st.title('Non-Biodegradable waste')
st.markdown(''' Non-Biodegradable waste (dry waste) can be catagorised as follows :
''')
asd  = st.columns(6)





