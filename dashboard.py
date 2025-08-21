import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


# TODO: Com uma visão mensal
# TODO: Faturamento por unidade
# TODO: Tipo de produto mais vendido
# TODO: Desempenho das formas de pagamento
# TODO: Como estão as avaliações das filiais?

df = pd.read_csv("supermarket_sales.csv", sep=",", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered