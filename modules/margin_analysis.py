import streamlit as st
import plotly.express as px

def display_margin_analysis(df_filtered):
    """
    Exibe análise de margem por produto e cidade
    """
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
