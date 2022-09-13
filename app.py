import streamlit as st
import joblib
model = joblib.load('virat')
st.title('Virat Centuries')
input = st.text_input('enter the score and Batting order')
output = model.predict([input])
if st.button('PREDICT'):
  st.title(output[0])
         
   
    
    
    
