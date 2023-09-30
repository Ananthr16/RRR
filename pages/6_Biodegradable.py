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



