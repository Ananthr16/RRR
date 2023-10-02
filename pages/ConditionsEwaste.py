import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('E-Waste')

st.title('Conditions to hand over E-Waste to commercials recyclers')

st.markdown(''' 
Remove Batteries: If possible, remove batteries from devices.
Batteries should be recycled separately because they can contain hazardous materials.

\n Remove Accessories: Detach any peripherals, cables, or accessories from the electronic devices. These can often be recycled separately.

\n Separate Components: If you have the knowledge and tools, consider disassembling the electronic devices into their main components, such as circuit boards, plastics, and metals.
Separating components can facilitate more efficient recycling.

\n Check for Hazardous Materials: Identify any hazardous materials present in your e-waste, such as mercury-containing bulbs, and ensure they are handled and recycled separately according to local regulations.

\n Label Hazardous Items: Clearly label any hazardous materials or components so that the recycling organization is aware of their presence.

''')
