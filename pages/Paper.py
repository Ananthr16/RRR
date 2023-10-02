import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')

st.set_page_config(initial_sidebar_state = 'collapsed',layout = 'wide')


st.title('Paper Waste')
st.markdown(''' Paper waste can be recycled completely, the conditions for paper to be recycled are given here 
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
