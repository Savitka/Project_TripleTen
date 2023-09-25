# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:23:50 2023

@author: savit
"""
import streamlit as st
import pandas as pd 
import plotly.express as px

#df=pd.read_csv('/Users/savit/Documents/GitHub/Project_TripleTen/vehicles_us.csv')
df=pd.read_csv('vehicles_us.csv')
#st.header('Car popularity analysis', divider='rainbow')
st.header('Car popularity analysis')

show_table = st.checkbox('Show data table slice')
if show_table :
    st.write("""
    ### Data table slice
    """)
    st.table(df.head(10))



st.write("""
### Proportions of car bodystyles
""")
grouped_bodystyle=df.groupby(['type'])['model'].nunique().reset_index()
grouped_bodystyle_sorted= grouped_bodystyle.sort_values(by = 'model',ascending=False)

#histogram

histogram = px.bar(grouped_bodystyle_sorted, x=grouped_bodystyle_sorted.type, y=grouped_bodystyle_sorted.model)
histogram.update_layout(title="<b> Percentage breakdown by car bodystyle")
show_histogram_bodystyle = st.checkbox('Show the histogram of proportions of car bodystyle')
if show_histogram_bodystyle :
    st.plotly_chart(histogram)


#Scatter plots 
st.write("""
### Scatter plot of car model and price
""")
show_scatter_plot = st.checkbox('Show the scatter plot of car model and price')
if show_scatter_plot:
    fig = px.scatter(df, x='price', y='model', color='type')
    st.plotly_chart(fig)



#Scatter plots + selectbox
st.write("""
### Scatter plot of the relationship between car model and price depending on the bodystyle
""")
show_scatter_plot_bodystyle = st.checkbox('Show the scatter plot of the relationship between car model and price depending on the bodystyle')
if show_scatter_plot_bodystyle:
    st.text('You can filtered data however you want')
    rest_type = df['type'].unique()
    make_choice = st.sidebar.selectbox('Select type:', rest_type)
    filtered_type = df[df.type==make_choice]
    fig = px.scatter(filtered_type, x='price', y='model', color='type')
    st.plotly_chart(fig)









