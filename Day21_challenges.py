import streamlit as st 
import time 

st.title('st.progress - updated progress bar')

with st.expander('About this app'):
    st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

st.write("Every 0.2 second the bar would move 1%")

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.2)
    my_bar.progress(percent_complete+1)

st.balloons()