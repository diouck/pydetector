import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.sidebar.write("Menu")
st.title("Test Titre")
st.markdown("<h3 style='color:red'> Dataframe</h2>",unsafe_allow_html=True)
df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)