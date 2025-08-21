import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


# TODO: Tipo de produto mais vendido
# TODO: Desempenho das formas de pagamento
# TODO: Como estão as avaliações das filiais?

df = pd.read_csv("supermarket_sales.csv", sep=",", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]
#df_filtered

# O Streamlit vai sempre criando de cima para baixo
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_fatdate = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_fatdate, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City",
 title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)


