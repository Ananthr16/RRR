import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Plastic')

st.title(''' Conditions to give plastic waste to recycling organisations :
''')
st.markdown(''' 
Clean the Plastics: Remove any food residue, liquids, or contaminants from the plastic items. 
Rinse bottles, containers, and other plastic products thoroughly. 
Clean plastics are easier to process and are less likely to contaminate the recycling stream.
\n 
Remove Non-Recyclables: Ensure that the plastic waste you're recycling doesn't contain non-recyclable materials or items that can't be processed, such as metal components, glass, or hazardous materials.
These contaminants can disrupt the recycling process and reduce the quality of the recycled material.
''')


	    
