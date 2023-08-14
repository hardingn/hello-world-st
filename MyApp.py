# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:30:17 2023

@author: Nicholas.Harding
"""

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
st.header('st.write')

# Example 1

st.write('Hello, world!* :sunglasses:')

# Ex 2

st.write(1234)

# Ex 3

df = pd.DataFrame({
    'first col':[1,2,3,4],
    'second col':[10,20,30,40]
    })
st.write(df)

# Ex 4
st.write('Below is a dataframe', df, 'above is a dataframe')

# Ex 5

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c'])
st.write(c)
