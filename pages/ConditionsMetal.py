import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Metal')

st.title('Conditions to recycle metal waste')
st.markdown('''
\n Cleanliness: Metal waste should be cleaned to remove contaminants such as dirt, oil, or grease. 
Clean metals are easier to process and yield higher-quality recycled materials.
\n Separation: Metals should be separated by type to facilitate recycling. 
Commonly recycled metals include aluminum, steel, copper, brass, and others. 
Separating them at the source streamlines the recycling process.
\n No Mixing with Non-Metals: Metal waste should not be mixed with non-metallic materials like plastics, glass, or organic waste. 
Such contamination can impede the recycling process and affect the quality of the recycled metal.
\n Size Reduction (if necessary): Large metal items may need to be reduced in size before recycling, either by cutting, crushing, or shredding. 
This makes them more manageable for processing.
''')
