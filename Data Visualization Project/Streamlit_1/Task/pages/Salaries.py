from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px


root = Path(__file__).resolve().parents[3]

st.write("Root:", root)
st.write("Files in root:")
st.write(list(root.iterdir()))


BASE_DIR = Path(__file__).resolve().parents[3]
csv_file = BASE_DIR / "ai_jobs_final.csv"

st.write("Current file:", csv_file)

# df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\Programming\Eng Mohammed\Data Visualization Project\ai_jobs_final.csv')

df = pd.read_csv(csv_file)


st.set_page_config('Salaries 💵↗️')

st.markdown('<h2 style="color:lightgreen;background-color:grey;font-size:40px;text-align:center;">Average salaries for each industry<h2/>', unsafe_allow_html=True)

# Selectbox , columns , containers ,metrics

industry_selected = st.selectbox(label='Select an industry 🏭' ,options=df.industry.unique())

col1,col2 = st.columns(2)

con1 = col1.container(border=True) # Not st.container 
con2 = col2.container(border=True)


# con1.metric not st. nor column.
con1.metric(label='The avg monthly salary',value=f'{round(df[df.industry == industry_selected].monthly_salary.mean())} $')
con2.metric(label='The avg annual salary',value=f'{round(df[df.industry == industry_selected].salary_usd.mean())} $')

