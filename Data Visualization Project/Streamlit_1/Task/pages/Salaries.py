from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

csv_file = Path("/mount/src/ai_jobs/Data Visualization Project/ai_jobs_final.csv")

root = Path(__file__).resolve().parents[3]

st.write("Exists:", csv_file.exists())
try:
    df = pd.read_csv(csv_file)
    st.write(df.head())
except Exception as e:
    st.exception(e)


st.write("Current file:", Path(__file__).resolve())
st.write("Parent 1:", Path(__file__).resolve().parent)
st.write("Parent 2:", Path(__file__).resolve().parents[1])
st.write("Parent 3:", Path(__file__).resolve().parents[2])
st.write("Root:", root)
st.write("Files in root:")
st.write(list(root.iterdir()))


BASE_DIR = Path(__file__).resolve().parents[3]


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

