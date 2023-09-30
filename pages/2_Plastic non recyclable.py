import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('app')
st.title('Non recyclable plastic waste')
cl=st.columns(2)
with cl[0]:
	st.markdown('''Non-recyclable plastic waste refers to types of plastic materials that are not easily or economically recyclable through conventional recycling processes.
These materials are typically difficult to recycle due to various reasons, such as their composition, contamination, or the lack of recycling infrastructure and technology to handle them effectively.
''')
	st.markdown('''The most commonly recycled plastics are:
•	1 – Polyethylene Terephthalate (PET) – water bottles and plastic trays
•	2 – High Density Polyethylene (HDPE) – milk cartoons and shampoo bottles
•	5 – Polypropylene (PP) – margarine tubs and ready-meal trays
Somewhat recyclable plastics (at specialist facilities) include:
•	3 – Polyvinyl Chloride (PVC) – piping
•	4 – Low Density Polyethylene (LDPE) – food bags
•	6 – Polystyrene (PS) – plastic cutlery
Incredibly hard to recycle plastics include crisp packets, salad bags, plastic wrap and more.

''')
	st.markdown(''' Recycler for non recyclable plastic waste - Rudra Environment solutions Ltd
''')
	st.markdown('''All plastic waste much be clean and dry. Proper care must be taken to ensure there is no wet waste mixed.''')
	st.markdown('''Contact information - 020 25448900, 9373053235''') 




