import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')

column = st.columns(2)
with column[0]:
	
	st.title('Plastic Waste')
	st.markdown('''Plastic waste is a pressing environmental issue with far-reaching consequences.
\n It refers to discarded plastic products and materials that accumulate in landfills, oceans, and natural habitats.
''')

	st.markdown(''' 
\n Plastic waste can be repurposed into creative household items. To get innovative ideas on how plastic waste can be repurposed use the AI Model.
\n Recycling of plastic waste can be done only in dedicated plastic recycling facilites 
''')
	if st.button('AI-Model'):
		switch_page('AI Model')

	st.markdown('''
\n The precautions to be taken with respect to plastic before handing it over to recyclers are given below : ''')
	if st.button('Conditions for recycling plastic waste'):
		switch_page('ConditionsPlastic')




	st.markdown(''' The contacts for organisations which collect plastic waste which is to be recycled are given below
\n a) For non-recyclable Plastic waste - Rudra Environment Solutions Ltd.
Contact - 020 25448900, 9373053235
\n b) For recyclable Plastic waste - Scrapcash   Contact - 9112323252
''')


with column[1]:
	st.image('Plastic waste.png')



