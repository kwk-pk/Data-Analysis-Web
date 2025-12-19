import streamlit as st
import pandas as pd

st.write("Hello World")

name = st.text_input("What  is your name?")

st.write("Hello ", name)

if st.button("Click me!"):
    st.write("Why do you do that?")

df = pd.read_csv('sustainable_waste_management_dataset_2024.csv')
                 
st.dataframe(df)

from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)),  columns=["a", "b", "c"])

st.bar_chart(df)
st.area_chart(df)

option = st.selectbox("Which ares do you like best?", ['Riverside', 'OldTown', 'UnivercityZone', 'IndustrailPark', 'SuburbEast', 'SuburbWest'])
st.write("You selected: ", option)

col1, col2, col3 = st.columns(3)

col1.header("Column 1")
col1.write("Hello column 1")

col2.header("Column 2")

col3.header("Column 3")
col3.write("Hello column 3")

container = st.container(border=True)
container.header("Container")