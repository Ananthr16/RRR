import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')



column = st.columns(2)
with column[0]:
	st.title('Paper Waste')
	st.markdown(''' Paper waste refers to discarded or unused paper products that are no longer needed or have reached the end of their useful life. 
\n It encompasses any paper materials that are thrown away, recycled, or otherwise disposed of in a manner that does not involve their continued use.
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
with column[1]:
	st.image('Paper waste.png')
