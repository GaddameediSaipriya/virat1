import streamlit as st
import joblib
model = joblib.load('virat')
st.title('Virat Centuries')
input = st.text_input('enter the score and Batting order')
output = model.Predict([input])
if st.button('predict'):
  st.title(output[0])
       
    
    
    
    
