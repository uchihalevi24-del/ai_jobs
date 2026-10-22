import streamlit as st
import pandas as pd

df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Programming\Eng Mohammed\Data Visualization Project\ai_jobs_final.csv')

st.set_page_config('AI jobs')

st.header('🙂 AI Jobs Data Analysis 2025')

st.subheader('This page shows an analysis for AI jobs dataset')

st.dataframe(df.head(10))