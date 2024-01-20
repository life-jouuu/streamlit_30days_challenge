import streamlit as st 

st.header('st.multiselect')
fav_colors_options = st.multiselect('What are your favorite colors?',["Blue", "Orange", "Green", "Red", "Yellow", "Purple"],["Red", "Yellow"])
st.write(fav_colors_options)