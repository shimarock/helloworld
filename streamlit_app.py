import streamlit as st
from datetime import datetime

# サイドバーで選択肢を設定
option = st.sidebar.selectbox(
    'Choose an example:',
    ('Example 1: Slider', 'Example 2: Range slider', 'Example 3: Range time slider', 'Example 4: Datetime slider')
)

# 例1
if option == 'Example 1: Slider':
    st.subheader('Slider')
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

# 例2
elif option == 'Example 2: Range slider':
    st.subheader('Range slider')
    values = st.slider(
         'Select a range of values',
         0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)

# 例3
elif option == 'Example 3: Range time slider':
    st.subheader('Range time slider')
    
    # 分単位での時間範囲を選択
    appointment_range = st.slider(
        "Schedule your appointment:",
        min_value=0,
        max_value=24 * 60 - 1,  # 1日の分数
        value=(11 * 60 + 30, 12 * 60 + 45)  # 初期値を11:30から12:45に設定
    )
    
    # 分を時間と分に変換
    appointment_start = time(appointment_range[0] // 60, appointment_range[0] % 60)
    appointment_end = time(appointment_range[1] // 60, appointment_range[1] % 60)
    
    st.write("You're scheduled for:", appointment_start, "to", appointment_end)

# 例4
elif option == 'Example 4: Datetime slider':
    st.subheader('Datetime slider')
    start_time = st.slider(
         "When do you start?",
         min_value=datetime(2020, 1, 1, 0, 0),
         max_value=datetime(2020, 12, 31, 23, 59),
         value=datetime(2020, 1, 1, 9, 30),
         format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)
