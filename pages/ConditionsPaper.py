import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Paper')

st.title('Conditions to hand over Paper waste to commercials recyclers')

st.markdown(''' Segregate clean and dry paper and cardboard at source, bring to RRC ''')
st.markdown(''' 
Remove Staples and Paperclips: Remove any staples, paperclips, or other metal fasteners from the paper. Small metal pieces can damage recycling machinery.
\n Flatten Cardboard: Flatten cardboard boxes to save space and make transportation easier. This also helps prevent unnecessary waste in recycling bins.
\n Avoid Contaminated Paper:Avoid recycling paper that is heavily contaminated with materials like wax, plastic coatings, or foil. These can be challenging to recycle and may need to be disposed of separately.
\n Clean the Paper: Try to remove any food residue, liquids, or other contaminants from the paper. Paper that is heavily soiled or contaminated may not be suitable for recycling.
''')
