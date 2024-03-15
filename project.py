# ------ Importing Packages -------
import pandas as pd
import streamlit as st
import matplotlib as plt
import seaborn as sns

# ------ Configuring Page -------

st.set_page_config(page_title= 'Average Time Spent By A User On Social Media',
                   page_icon= ':bar_chart:',
                   layout = 'centered')

df = pd.read_csv('dummy_data.csv')

print(df.head(5))

st.title('Data Project 1:')
st.header('Average Time Spent By A User On Social Media')
st.write('by: Lexin Deang')
st.caption('Kaggle Dataset Link : https://www.kaggle.com/datasets/imyjoshua/average-time-spent-by-a-user-on-social-media')
st.dataframe(df)