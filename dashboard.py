import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# Carregar dados
df = pd.read_csv("supermarket_sales.csv", sep=",", decimal=",")

# FORÇAR a coluna Total a ser numérica desde o início
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["gross income"] = pd.to_numeric(df["gross income"], errors="coerce")
df["Tax 5%"] = pd.to_numeric(df["Tax 5%"], errors="coerce")
df["cogs"] = pd.to_numeric(df["cogs"], errors="coerce")
df["Unit price"] = pd.to_numeric(df["Unit price"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["gross margin percentage"] = pd.to_numeric(df["gross margin percentage"], errors="coerce")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Adicionar colunas temporais
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
df["DayOfWeek"] = df["Date"].dt.day_name()
df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour

# Sidebar com filtros
st.sidebar.header("📊 Filtros")
month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique())
city_filter = st.sidebar.multiselect("Selecione as cidades", df["City"].unique(), default=df["City"].unique())
product_filter = st.sidebar.multiselect("Selecione as linhas de produto", df["Product line"].unique(), default=df["Product line"].unique())

# Aplicar filtros
df_filtered = df[
    (df["Month"] == month) & 
    (df["City"].isin(city_filter)) & 
    (df["Product line"].isin(product_filter))
]

# Título principal
st.title("📈 Dashboard de Vendas - Supermercado")
st.markdown(f"**Período:** {month} | **Cidades:** {', '.join(city_filter)} | **Produtos:** {', '.join(product_filter)}")

# ===== KPIs PRINCIPAIS =====
st.header("🎯 KPIs Principais")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sales = df_filtered["Total"].sum()
    st.metric("💰 Faturamento Total", f"${total_sales:,.2f}")
    
with col2:
    avg_ticket = df_filtered["Total"].mean()
    st.metric("🎫 Ticket Médio", f"${avg_ticket:.2f}")
    
with col3:
    total_transactions = len(df_filtered)
    st.metric("🛒 Total de Transações", f"{total_transactions:,}")
    
with col4:
    avg_rating = df_filtered["Rating"].mean()
    st.metric("⭐ Avaliação Média", f"{avg_rating:.1f}")

# ===== ANÁLISE TEMPORAL AVANÇADA =====
st.header("🕒 Análise Temporal")

# Gráfico de vendas por dia da semana
col1, col2 = st.columns(2)

with col1:
    day_sales = df_filtered.groupby("DayOfWeek")["Total"].sum().reset_index()
    # Ordenar dias da semana corretamente
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_sales = day_sales.set_index('DayOfWeek').reindex(day_order).reset_index()
    
    fig_day = px.bar(
        day_sales, 
        x="DayOfWeek", 
        y="Total", 
        title="📅 Vendas por Dia da Semana",
        color="Total",
        color_continuous_scale="viridis"
    )
    fig_day.update_layout(xaxis_title="Dia da Semana", yaxis_title="Faturamento ($)")
    st.plotly_chart(fig_day, use_container_width=True)

# Gráfico de vendas por hora
with col2:
    hour_sales = df_filtered.groupby("Hour")["Total"].sum().reset_index()
    fig_hour = px.line(
        hour_sales, 
        x="Hour", 
        y="Total", 
        title="⏰ Vendas por Hora do Dia",
        markers=True
    )
    fig_hour.update_layout(xaxis_title="Hora", yaxis_title="Faturamento ($)")
    st.plotly_chart(fig_hour, use_container_width=True)

# ===== TOP PRODUTOS POR FATURAMENTO =====
st.header("🏆 Top Produtos")

# Top produtos por faturamento
top_products = df_filtered.groupby("Product line")["Total"].sum().sort_values(ascending=False).reset_index()
top_products["Percentage"] = (top_products["Total"] / top_products["Total"].sum() * 100).round(1)

fig_top_prod = px.bar(
    top_products,
    x="Total",
    y="Product line",
    orientation="h",
    title="📊 Top Produtos por Faturamento",
    text=top_products["Total"].apply(lambda x: f"${x:,.0f}"),
    color="Total",
    color_continuous_scale="plasma"
)
fig_top_prod.update_layout(yaxis_title="Linha de Produto", xaxis_title="Faturamento ($)")
fig_top_prod.update_traces(textposition='outside')
st.plotly_chart(fig_top_prod, use_container_width=True)

# ===== SEGMENTAÇÃO DE CLIENTES =====
st.header("👥 Segmentação de Clientes")

col1, col2 = st.columns(2)

# Análise por tipo de cliente
with col1:
    customer_type_analysis = df_filtered.groupby("Customer type").agg({
        "Total": ["sum", "mean", "count"],
        "Rating": "mean"
    }).round(2)
    customer_type_analysis.columns = ["Faturamento Total", "Ticket Médio", "Nº Transações", "Avaliação Média"]
    
    st.subheader("📋 Análise por Tipo de Cliente")
    st.dataframe(customer_type_analysis, use_container_width=True)

# Análise por gênero
with col2:
    gender_analysis = df_filtered.groupby("Gender").agg({
        "Total": ["sum", "mean", "count"],
        "Rating": "mean"
    }).round(2)
    gender_analysis.columns = ["Faturamento Total", "Ticket Médio", "Nº Transações", "Avaliação Média"]
    
    st.subheader("👤 Análise por Gênero")
    st.dataframe(gender_analysis, use_container_width=True)

# Gráfico de distribuição por tipo de cliente
fig_customer = px.pie(
    df_filtered.groupby("Customer type")["Total"].sum().reset_index(),
    values="Total",
    names="Customer type",
    title="💳 Distribuição de Faturamento por Tipo de Cliente"
)
st.plotly_chart(fig_customer, use_container_width=True)

# ===== PERFORMANCE POR FILIAL =====
st.header("🏢 Performance por Filial")

col1, col2 = st.columns(2)

# Performance por filial
with col1:
    branch_performance = df_filtered.groupby("Branch").agg({
        "Total": ["sum", "mean", "count"],
        "Rating": "mean"
    }).round(2)
    branch_performance.columns = ["Faturamento Total", "Ticket Médio", "Nº Transações", "Avaliação Média"]
    
    st.subheader("📊 Performance por Filial")
    st.dataframe(branch_performance, use_container_width=True)

# Performance por cidade
with col2:
    city_performance = df_filtered.groupby("City").agg({
        "Total": ["sum", "mean", "count"],
        "Rating": "mean"
    }).round(2)
    city_performance.columns = ["Faturamento Total", "Ticket Médio", "Nº Transações", "Avaliação Média"]
    
    st.subheader("🌍 Performance por Cidade")
    st.dataframe(city_performance, use_container_width=True)

# Gráfico comparativo filial vs cidade
fig_branch_city = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Faturamento por Filial", "Faturamento por Cidade"),
    specs=[[{"type": "bar"}, {"type": "bar"}]]
)

# Filial
branch_total = df_filtered.groupby("Branch")["Total"].sum().reset_index()
fig_branch_city.add_trace(
    go.Bar(x=branch_total["Branch"], y=branch_total["Total"], name="Filial", marker_color="lightblue"),
    row=1, col=1
)

# Cidade
city_total = df_filtered.groupby("City")["Total"].sum().reset_index()
fig_branch_city.add_trace(
    go.Bar(x=city_total["City"], y=city_total["Total"], name="Cidade", marker_color="lightcoral"),
    row=1, col=2
)

fig_branch_city.update_layout(height=400, title_text="Comparativo: Filial vs Cidade")
st.plotly_chart(fig_branch_city, use_container_width=True)

# ===== ANÁLISE DE MARGEM =====
st.header("💰 Análise de Margem")

col1, col2 = st.columns(2)

# Análise de margem por produto
with col1:
    margin_by_product = df_filtered.groupby("Product line").agg({
        "gross income": "sum",
        "Total": "sum"
    }).reset_index()
    margin_by_product["Margem %"] = (margin_by_product["gross income"] / margin_by_product["Total"] * 100).round(2)
    
    fig_margin_prod = px.bar(
        margin_by_product,
        x="Product line",
        y="Margem %",
        title="📈 Margem por Linha de Produto",
        text=margin_by_product["Margem %"].apply(lambda x: f"{x}%"),
        color="Margem %",
        color_continuous_scale="RdYlGn"
    )
    fig_margin_prod.update_layout(xaxis_title="Linha de Produto", yaxis_title="Margem (%)")
    fig_margin_prod.update_traces(textposition='outside')
    st.plotly_chart(fig_margin_prod, use_container_width=True)

# Análise de margem por cidade
with col2:
    margin_by_city = df_filtered.groupby("City").agg({
        "gross income": "sum",
        "Total": "sum"
    }).reset_index()
    margin_by_city["Margem %"] = (margin_by_city["gross income"] / margin_by_city["Total"] * 100).round(2)
    
    fig_margin_city = px.bar(
        margin_by_city,
        x="City",
        y="Margem %",
        title="🌍 Margem por Cidade",
        text=margin_by_city["Margem %"].apply(lambda x: f"{x}%"),
        color="Margem %",
        color_continuous_scale="RdYlGn"
    )
    fig_margin_city.update_layout(xaxis_title="Cidade", yaxis_title="Margem (%)")
    fig_margin_city.update_traces(textposition='outside')
    st.plotly_chart(fig_margin_city, use_container_width=True)

# Resumo financeiro
st.subheader("📊 Resumo Financeiro")
financial_summary = df_filtered.agg({
    "Total": "sum",
    "gross income": "sum",
    "Tax 5%": "sum"
}).round(2)
financial_summary.index = ["Faturamento Total", "Lucro Bruto", "Impostos"]
st.dataframe(financial_summary, use_container_width=True)

# ===== GRÁFICOS ORIGINAIS (mantidos para compatibilidade) =====
st.header("📊 Visualizações Originais")

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_fatdate = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_fatdate, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City",
 title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

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

fig_payment = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por forma de pagamento")
col4.plotly_chart(fig_payment, use_container_width=True)

rating_total = df_filtered.groupby("City")["Rating"].mean().reset_index()
fig_rating = px.bar(rating_total, x="City", y="Rating", title="Avaliação média por filial")
col5.plotly_chart(fig_rating, use_container_width=True)
