import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello world!")

with st.sidebar:
    st.header("About App")
    st.write("This is my first app !")
st.header("This is a header with a divider",divider='rainbow')

st.markdown("This is created using st.markdown.")

col1,col2=st.columns(2)

with col1:
    x=st.slider("Chose an x value",1,10)

with col2:
    st.write("The value of :blue[***x***]",x)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.markdown("This is in write formate")
st.write(df)

st.markdown("This is in table formate")
st.table(df)   
