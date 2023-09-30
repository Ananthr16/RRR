import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')

st.title('Paper Waste')
st.markdown(''' Paper waste can be recycled completely, the conditions for paper to be recycled are given here 
''')
if st.button('Conditions to recycle paper waste'):
	switch_page('ConditionsPaper')
st.markdown('''
Paper can be recycled through
\n a) 
\n b) 
\n c) 1. Establish convenient and accessible recycling and reuse collection centres (to be managed by local communities) 
for different types of materials (e.g., paper, cardboard, plastic, glass, metals, clothes, books, toys) and encourage citizens to deposit recyclables at these centres. 
Drop-off points can be set up throughout the community, including schools, markets, and public spaces
\n d) By commercial composting organisations.  ''')




st.markdown(''' The commercial composting organisation contacts are given below
\n MobiTrash - https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwil0ZiO7dKBAxXLP3AKHRm1AA0QFnoECAoQAQ&url=https%3A%2F%2Fwww.mobitrash.in%2F&usg=AOvVaw2CUH_i72_ZxySPZ98nhNgR&opi=89978449
''')
