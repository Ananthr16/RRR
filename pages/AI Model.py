#importing the libraries
import streamlit as st
from ultralytics import YOLO
import openai
from PIL import Image
import time
from streamlit_extras.switch_page_button import switch_page

#setting the page
if st.button('Back'):
	switch_page('app')
st.markdown("""Steps to use the AI Model :
- Click the image using the camera app on your mobile phone
- Press the button 'browse files' and choose the image from your gallery.
- select the correct combination from the ML Model outputs
- Select reduce,Reuse or recycle and wait for the results """)
object = []
type = []
@st.cache_resource
def loading() :
	#loading the models
	mod1 = YOLO('yolov8x-cls.pt')
	mod2 = YOLO('best.pt')
	return mod1,mod2
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Set up the OpenAI API client
openai.api_key = "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"

#loading the image
img = st.file_uploader('Select your input image in jpg/jpeg',type=['jpg','png','jpeg'])

#function for the search item
def search(pr):
	completion =openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"assistant","content":pr}])
	response = completion['choices'][0]['message']['content']
	return response
#processing
if img is not None:
	img = Image.open(img)
	st.image(img)
	model1,model2=loading()
	col1,col2 = st.columns(2)
	res1 = model1.predict(img)
	res2 = model2.predict(img)
	two = res2[0].probs.top5
	col1.header('Object Classification')
	for name in res1[0].probs.top5:
		col1.write(res1[0].names[name])
		object.append(res1[0].names[name])
	col2.header('Material Classification')
	for i in two:
		col2.write(res2[0].names[i])
		type.append(res2[0].names[i])
	st.header('Choose a combination of one value from both categories by defining the numbers below')
	col = st.columns(2)
	x = col[0].number_input('select the number for object',min_value = 0,max_value=5,step=1)
	y = col[1].number_input('select the number for type',min_value = 0,max_value=5,step=1)
	time.sleep(1)
	if x >0 and y>0:
		string = type[y-1]+" "+object[x-1]
		st.write(string)
	col1, col2, col3 = st.columns(3)
	with col1:
		button1 = st.button('Recycle')
	with col2:
		button2 = st.button('Reduce')
	with col3:
		button3 = st.button('Reuse')

	if button1:
		st2 = f'Give me 5 innovative ways to recycle {string} waste'
		st.write(search(st2))
	if button2:
		st2 = f'Give me 5 eco-friendly alternatives to {string} and ways to reduce {string}'
		st.write(search(st2))
	if button3:
		st2 = f'Give me 3 ways to reuse {string} in a very detailed/step by step manner'
		st.write(search(st2))
