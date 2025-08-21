import streamlit as st
import plotly.express as px

def display_customer_analysis(df_filtered):
    """
    Exibe análise de segmentação de clientes
    """
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
