# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:59:16 2023

@author: savit
"""

import streamlit as st
import pandas as pd 

st.write("""
### Reading info on our dataset
""")
st.write("""
### Head of data
""")

df=pd.read_csv('C:/Users/savit/Documents/GitHub/Project_TripleTen/vehicles_us.csv')
st.table(df.head())

#Investigate the proportion of the various types of establishments. Plot a graph.

st.write("""
### Proportions of the varioous types of establishments
""")

grouped_est=df.groupby(['type'])['model'].nunique().reset_index()
st.table(grouped_est)

## showing how plotly works

#import plotly.graph_objects as go
#from plotly import tools
#import plotly.offline as py
import plotly.express as px

fig2 = px.pie(grouped_est, values=grouped_est.model, names=grouped_est.type)
fig2.update_layout(title="<b> Split by establishment")
st.plotly_chart(fig2)

## Filtering the data

st.write("""
### Block with Filtered Data
""")
st.text('You can filtered data however you vant')
rest_type = df['type'].unique()
make_choice = st.sidebar.selectbox('Select your establishment:', rest_type)
filtered_type = df[df.type==make_choice]
st.table(filtered_type)