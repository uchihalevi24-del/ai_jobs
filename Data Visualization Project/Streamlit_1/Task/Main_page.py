from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

# df = pd.read_csv(r'/Data Visualization Project / ai_jobs_final.csv')
BASE_DIR = Path(__file__).resolve().parents[2]
csv_file = BASE_DIR / "ai_jobs_final.csv"

df = pd.read_csv(csv_file)


st.set_page_config('Main Page 🏠')

st.markdown('<h1 style="color:lightpink;background-color:purple;border-radius:20px;padding-left:70px;">🤖  AI jobs 2025 data analysis 🤖<h1/>',unsafe_allow_html=True)

st.subheader('This is a sample of the AI jobs dataset ')

st.dataframe(df.head())

st.divider()

st.subheader('A simple relation chart ⬇️')

salary_exp_lvl =  df.groupby('experience_level')['monthly_salary'].mean().reset_index().sort_values(by='monthly_salary')

st.plotly_chart(px.bar(salary_exp_lvl,x='experience_level',y='monthly_salary',
                       title='The relation between monthly salary and experience level',
                       color='experience_level',
                       template='simple_white',
                       labels={'experience_level' : 'Experience Level' , 'monthly_salary' : 'Monthly Salary'}))
