import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('app')

column = st.columns(2)
with column[0]:
	
	st.title('Hazardous Waste')
	st.markdown(''' Hazardous waste refers to any waste material that poses a substantial threat to human health, the environment, or both, due to its chemical, physical, or biological characteristics.
\n These wastes are typically produced by industrial processes, laboratories, and various other sources, but some hazardous materials can also be found in common household products.
\n Mixing hazardous waste with normal waste can have serious consequences, including environmental contamination and health risks.
\n Here are some common household hazardous wastes and the potential consequences of improper disposal:


''')
	st.subheader('The precautions to be taken with respect to kitchen waste before composting is given here ')
	st.markdown(''' Chemical Product Labels: Read product labels carefully, follow usage instructions, and dispose of the empty containers as hazardous waste if necessary.
\nLocal Household Hazardous Waste Collection: Many communities have designated collection programs or facilities for household hazardous waste. Take advantage of these services for safe disposal.
''')




	st.markdown(''' The commercial Hazardous waste recycling organisations contacts are given below
\n BIOMEDICAL WASTE - PASSCO(Injection needles, dressing material to be kept separately at home). Contact - 020 25467096 
''')

with column[1]:
	st.image('Hazardous waste.png')



