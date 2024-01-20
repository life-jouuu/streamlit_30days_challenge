import streamlit as st 

st.header('st.selectbox')
option = st.selectbox("What's your fav color?",('Blue','Yellow','Orange','Green','Red'))

st.write('Your favorite color is: ',option)