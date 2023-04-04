#this is the main file
import streamlit as st
import numpy as np
st.title("Hoorah the application is deployed")

st.write("Let's list few more")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
