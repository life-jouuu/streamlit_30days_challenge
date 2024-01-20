import streamlit as st
from datetime import time, datetime

st.header('st.slider 建立Slider')

st.subheader('Slider')
st.write( '用st.slider(文字,滑桿的min value, 滑桿的max value, default value)')
age = st.slider('How old are you?',0,130,25)
st.write("I'm",age,"years old.")

st.subheader('Range slider')
values = st.slider('Select a range of values', 0.0,100.0,(25.00,75.00))
st.write('Values:',values)

st.subheader('Range time slider')
st.write("時間用 value=( time(hh : mm),time(hh : mm))")
appointment = st.slider('Schedule your appointment: ', value=(time(11,30), time(12,45)))
st.write("you're scheduled for: ", appointment)

st.subheader('Datetime slider')
start_time = st.slider( "when do you start?", value = datetime(1998,4,10,23,8), format = "MM/DD/YY - hh:mm")
st.write("Start time: ", start_time )