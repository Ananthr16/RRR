import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')



st.title('Glass Waste')
st.markdown(''' Glass waste is a crucial component of sustainable waste management.
Glass is a versatile material that can be endlessly recycled without a loss in quality, making it an environmentally friendly option. 
''')
st.markdown('''
The precautions to be taken with respect to Glass Waste before handing over to commercial recyclers are given below : ''')
if st.button('Conditions for Glass Waste recycling'):
		switch_page('ConditionsGlass')




st.markdown(''' The commercial Glass recycling organisation's contacts are given below
\n ScrapCash - Siddhant Ingale : 9112323252, Zuber Sayyed : 8308133133

''')
