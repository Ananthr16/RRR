import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('app')

st.title('Biodegradable Waste')
st.markdown(''' Biodegradable waste (organic) is generated from kitchen waste and garden waste 
\n Biodegradable waste should be composted.
\n Composting can be done:
\n a) At the individual household level. 
\n b) At the residential complex level.
\n c) At the community level.
\n d) By commercial composting organisations. 
''')
st.markdown('''
The precautions to be taken with respect to kitchen waste before composting is given here : ''')


st.markdown(''' The commercial composting organisation contacts are given below
\n MobiTrash - https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwil0ZiO7dKBAxXLP3AKHRm1AA0QFnoECAoQAQ&url=https%3A%2F%2Fwww.mobitrash.in%2F&usg=AOvVaw2CUH_i72_ZxySPZ98nhNgR&opi=89978449
''')

