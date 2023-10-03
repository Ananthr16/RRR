import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')

st.image('E-waste.png')

st.title('E-Waste')
st.markdown(''' E-waste, short for electronic waste, refers to discarded electronic and electrical equipment that has reached the end of its useful life. 
This category of waste includes a wide range of devices and appliances, such as smartphones, laptops, televisions, refrigerators, and more. 
''')
st.markdown('''
The precautions to be taken with respect to E-Waste before handing it over to commercial E-Waste recycling organisations are given below : ''')
if st.button('Conditions for E-Waste'):
		switch_page('ConditionsEwaste')




st.markdown(''' The commercial E-Waste recycling oragnisations and their contacts are given below
\n Scrapcash - Siddhant Ingale : 9112323252 
\n Poornam Ecovision - Supriya Kokane : 7558324287
\n Hi Tech RecyclingIndia - Manoj Patil : 020 66521000
''')







