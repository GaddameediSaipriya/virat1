import streamlit as st
import joblib
model = joblib.load('virat')
st.title('Virat Centuries')
input = st.text_input('enter the Score and Batting order')
output = model.predict([input])
if st.button('predict'):
  st.title(output[0])
      
                              
                                                                
