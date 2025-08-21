import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# TODO: Tipo de produto mais vendido
# TODO: Desempenho das formas de pagamento
# TODO: Como estão as avaliações das filiais?

# Carregar dados
df = pd.read_csv("supermarket_sales.csv", sep=",", decimal=",")

# FORÇAR a coluna Total a ser numérica desde o início
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

# O Streamlit vai sempre criando de cima para baixo
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_fatdate = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_fatdate)

fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City",
 title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod)

# Agrupamento por cidade com verificação robusta
city_total = df_filtered.groupby("City")["Total"].sum().reset_index()

# Criar gráfico com formatação adequada
fig_city = px.bar(
    city_total, 
    x="City", 
    y="Total", 
    title="Faturamento por filial",
    text=city_total["Total"].apply(lambda x: f"${x:,.0f}" if pd.notna(x) else "Erro")
)
fig_city.update_traces(textposition='outside')  # Posicionar texto fora das barras
col3.plotly_chart(fig_city)


