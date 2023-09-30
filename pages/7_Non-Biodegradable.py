import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('app')

st.title('Non-Biodegradable waste')


st.markdown('''
Non-Biodegradable waste can be reused or recycled 
\n The conditions for reuse/recycling of the above categories of waste are included in the respective page.
''')

   



st.markdown(''' Non-Biodegradable waste (dry waste) can be catagorised as follows :
''')
asd  = st.columns(6)

with asd[0]:
	if st.button("Paper"):
		switch_page('Paper')
		

with asd[1]:
	if st.button("Plastic"):
		switch_page('Plastic')

with asd[2]:
	if st.button("Glass"):
		switch_page('Glass')


with asd[3]:
	if st.button("Metal"):
		switch_page('Metal')


with asd[4]:
	if st.button("E-Waste"):
		switch_page('E-Waste')




with asd[5]:
	if st.button("Others"):
		switch_page('Others')



st.markdown('''
Non-Biodegradable waste can be reused or recycled 
\n The conditions for reuse/recycling of the above categories of waste are included in the respective page.
''')

   







