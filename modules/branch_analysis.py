import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def display_branch_analysis(df_filtered):
    """
    Exibe análise de performance por filial e cidade
    """
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
