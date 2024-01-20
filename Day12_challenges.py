import streamlit as st 


st.header('st.checkbox')
st.write('what would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
brownie = st.checkbox('Brownie')

if icecream:
    st.write("Great! Here's your :icecream:")
if coffee:
    st.write("Here you go! Here's your :coffee:")
if brownie:
    st.write(" Coming! :cake:")
