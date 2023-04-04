#this is the main file
import streamlit as st
import numpy as np
import pandas as pd
st.title("Hoorah the application is deployed")

st.write("Let's list few more")
print("/n")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
