
!pip install -q altair
!pip install -q streamlit

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st



st.header('st.write')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
