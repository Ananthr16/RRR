import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')


st.title('Metal Waste')
st.markdown(''' Metal waste generated from households consists of various items made of metal that are no longer needed or have reached the end of their usable life. 
Common examples include kitchen utensils, appliances, old furniture, bicycles, and metal containers.
''')
st.markdown('''
The precautions to be taken with respect to Metal waste before handing it over to recyclers is given below ''')
if st.button('Conditions for composting'):
		switch_page('ConditionsMetal')

st.markdown(''' In garden waste palm and coconut tree fronds (leaf) or the leaflets should not be included ''')


st.markdown(''' The commercial composting organisation contacts are given below
\n MobiTrash - https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwil0ZiO7dKBAxXLP3AKHRm1AA0QFnoECAoQAQ&url=https%3A%2F%2Fwww.mobitrash.in%2F&usg=AOvVaw2CUH_i72_ZxySPZ98nhNgR&opi=89978449
''')
