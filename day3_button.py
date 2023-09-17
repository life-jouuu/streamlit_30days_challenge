import streamlit as st

st.header('Click to say hello - st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
