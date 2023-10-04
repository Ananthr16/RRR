import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('Non-Biodegradable')




column = st.columns(2)
with column[0]:
	st.title('Other types of waste')
	st.markdown(''' Other types of waste includes Mats, rubber, coir, cotton, synthetic, Mops, Dusters, Footwear, Ceramic, Cosmetics, Wood, and Coconut shells
 ''')
	st.markdown(''' The recycling organisations that provide services to recycle these miscellaneous wastes ''')
	st.subheader('For footware')
	st.markdown('''- BAREFOOT FOUNDATION. The footware is to be tied in pairs and dropped at Joggers Park. 
 Contact for Barefoot Foundation - Sanyogita Kudale : 984808860 
 \n ''')
	st.subheader('For BEDSHEETS, CURTAINS, AND SOFA COVERS')
	st.markdown('''Call Mrs Lakhani & drop it at gate of Landmark Garden society, Kalyani Nagar.
Rajeshwari Lakhani: 9765606409
\n ''')
	st.subheader('For THERMOCOL (EPS- Expanded Polystyrene) NOT STYROFOAM (XPS- Extruded Polystyrene Foam)')
	st.markdown('''KK Nag Pvt Ltd. Contact - Ghare (RecyCole): 9021619509 OR Dipankar Nandi : 9373336522 
\n ''')
	st.markdown(''' G.D.Environmental Pvt Ltd. (GDEPL) - Abhijeet Datar (GDEPL) : 9822043916
n\ ''')
	st.subheader('To donate CLOTHES, TOYS, BOOKS')   
	st.markdown(''' \n Ishanya Foundation. Contact - Bindu Nair : 9960033433
\n Poornam EcovisionFoundation. Contact - Supriya Kokane: 7558324287
\n Swach VCollect. Conatct - Prasanna : 9765999494
''')


with column[1]:
	st.image('Miscellaneous.png', caption='Miscellaneous Waste')





















