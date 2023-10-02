import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')




st.title('Other types of waste')
st.markdown(''' Other types of waste includes Mats, rubber, coir, cotton, synthetic, Mops, Dusters, Footwear, Ceramic, Cosmetics, Wood, and Coconut shells
''')
if st.button('Conditions to recycle paper waste'):
	switch_page('ConditionsPaper')
	
st.markdown('''
Paper can be recycled through
\n a) Collection centres for recycling paper
\n b) Community recycling centres 
\n d) By commercial recyclers.  ''')




st.markdown(''' The commercial recyclers contacts are given below
\n Scrapcash 
contact details for Scrapcash : Siddanth Ingale 9112323252
''')

