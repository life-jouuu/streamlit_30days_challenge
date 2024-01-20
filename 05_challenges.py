import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Streamlit 30 days challenges - Day05 - st.write 用法')

st.write('1. 顯示文字與字體變化')
st.write('Hello, *World!* :sunglass:')
st.write('把文字用 ** 括號起來可以變成斜體、並可以用::打出Emoji!')
st.write(1234)

st.write('2. 顯示Dataframe')
df = pd.DataFrame ({
    'first col':[1,2,3,4],
    'second col':[10,20,30,40]
    })
st.write('直接把定義的dataframe抓進來 -> st.write(df)')
st.write(df)

st.write('2. 顯示Dataframe+文字 / 多個參數')
st.write('直接用st.write把想顯示的資料串起來 -> "st.write(below is a dataframe, df, above is a dataframe"')
st.write('below is a dataframe', df, 'above is a dataframe')

st.write('3. 顯示Dataframe - 顯示各種不同圖表')
st.write('假設我現在有個散點圖, 先用numpy定義一個三維度的dataframe, 在用altair做出想要的圖表')
df2 = pd.DataFrame( np.random.randn(200,3), columns = ['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', color = 'c', tooltip = ['a','b','c']
)
st.write(c)
