import streamlit as st
import plotly.express as px
import pandas as pd

def display_original_charts(df_filtered):
    """
    Exibe os gráficos originais do dashboard
    """
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
