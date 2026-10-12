import pandas as pd
import numpy as np
import streamlit as st

# 1. Add a page title and header
st.title("📊 Simple Streamlit Dashboard")
st.write("Welcome to your first app. Move the slider below to update the chart in real-time!")

# 2. Add an interactive slider widget
num_points = st.slider("Select number of data points:", min_value=10, max_value=100, value=50)

# 3. Generate some random data based on the slider input
chart_data = pd.DataFrame(
    np.random.randn(num_points, 2),
    columns=['Metric A', 'Metric B']
)

# 4. Display a line chart
st.subheader("Interactive Trend Line")
st.line_chart(chart_data)

# 5. Add a button to show the raw data grid
if st.button("Toggle Raw Data Table"):
    st.subheader("Raw Data View")
    st.dataframe(chart_data)
