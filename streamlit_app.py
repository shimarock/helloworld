import streamlit as st
from datetime import datetime, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import pydeck as pdk
import graphviz as gv

# グラフの選択肢
graphs = [
    "Line Chart",
    "Area Chart",
    "Bar Chart",
    "Matplotlib Plot",
    "Altair Chart",
    "Vega Lite Chart",
    "Plotly Chart",
    "Bokeh Chart",
    "Pydeck Chart",
    "Graphviz Chart",
    "Map",
]

# サイドバーで選択肢を設定
option = st.sidebar.selectbox(
    'Choose an example:',
    ('Example 1: Slider', 'Example 2: Range slider', 'Example 3: Range time slider', 'Example 4: Datetime slider')
)

# サイドバーでグラフの選択
selected_graph = st.sidebar.selectbox("Choose a graph:", graphs)

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

# サンプルデータの生成
np.random.seed(42)
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=["A", "B", "C"])

# 選択されたグラフの描画
if selected_graph == "Line Chart":
    st.line_chart(df)
elif selected_graph == "Area Chart":
    st.area_chart(df)
elif selected_graph == "Bar Chart":
    st.bar_chart(df)
elif selected_graph == "Matplotlib Plot":
    fig, ax = plt.subplots()
    ax.plot(df["A"])
    st.pyplot(fig)
elif selected_graph == "Altair Chart":
    chart = alt.Chart(df).mark_line().encode(x='A', y='B')
    st.altair_chart(chart)
elif selected_graph == "Vega Lite Chart":
    st.vega_lite_chart(df, {"mark": "line", "encoding": {"x": "A", "y": "B"}})
elif selected_graph == "Plotly Chart":
    fig = px.line(df, x="A", y="B")
    st.plotly_chart(fig)
elif selected_graph == "Bokeh Chart":
    # Bokehの例を追加
    pass
elif selected_graph == "Pydeck Chart":
    view_state = pdk.ViewState(latitude=37.7749, longitude=-122.4194, zoom=10, pitch=0)
    r = pdk.Deck(map_style="mapbox://styles/mapbox/light-v9", initial_view_state=view_state)
    st.pydeck_chart(r)
elif selected_graph == "Graphviz Chart":
    dot = gv.Digraph()
    dot.node('A')
    dot.node('B')
    dot.edge('A', 'B')
    st.graphviz_chart(dot)
elif selected_graph == "Map":
    map_data = pd.DataFrame({'lat': [37.7749], 'lon': [-122.4194]})
    st.map(map_data)