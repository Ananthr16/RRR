import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Glass')

st.title('Conditions to be met before handing over Glass waste to commercial recycling organisations')
st.markdown('''
\n
Clean the Glass: Remove any food residue, liquids, or contaminants from glass containers, such as bottles and jars. 
 Rinse them thoroughly to ensure they are free from residue. 
 Clean glass is easier to recycle and reduces the risk of contamination in the recycling stream.

\n Remove Caps and Lids: Take off any metal or plastic caps, lids, or corks from glass containers. 
These materials are not typically recyclable with glass and can disrupt the recycling process.

\n Do Not Mix with Non-Recyclables: Never mix glass waste with non-recyclable materials, such as hazardous waste, electronic waste, or household trash.
Properly dispose of non-recyclable items through the appropriate channels.

''')
