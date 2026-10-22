import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Programming\Eng Mohammed\Data Visualization Project\ai_jobs_final.csv')

st.set_page_config('Salary',layout='wide')


Q7 = df.groupby('job_title')['monthly_salary'].mean().reset_index().sort_values(by='monthly_salary')

st.markdown('<h1 style="color:lightgrey ; font-size : 40px; text-align:center" >The relation between job title and monthly salary<h1/>' , unsafe_allow_html=True)

st.plotly_chart(px.bar(Q7,x='job_title',y='monthly_salary'
       ,labels={'monthly_salary':'Monthly Salary','job_title':'Job Title'}
       ,template='plotly_dark'
       ,color_continuous_scale='plotly3'
       ,color='monthly_salary')
)

st.divider()

st.markdown('<h1 style="color:lightgreen;font-size:40px;text-align:center;">Average salaries for each job<h1/>', unsafe_allow_html=True)

job = st.selectbox(label='Choose a job' , options=df.job_title.unique())

col1,col2 = st.columns(2)

con1 = col1.container(border=True)
con2 = col2.container(border=True)


con1.metric(label='The avg monthly salary',value=f'{round(df[df.job_title == job].monthly_salary.mean())} $')
con2.metric(label='The avg annual salary',value=f'{round(df[df.job_title == job].salary_usd.mean())} $')

