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




st.markdown(''' The commercial metal recycling organisation contacts are given below
\n ScrapCash -  Zuber Sayyed : 8308133133, 
\n ScrapCash - Siddhant Ingale : 9112323252
''')
