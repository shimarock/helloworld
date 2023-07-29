import streamlit as st
from datetime import date, datetime

st.header('st.slider')

#例1

st.subheader('Slider')

age = st.slider('年齢はいくつですか？', 0, 130, 25)
st.write('私の年齢は', age, 'です')

#例2

st.subheader('Range slider')

values = st.slider(
    '値の範囲を選択してください'
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


#例3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

#例4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)