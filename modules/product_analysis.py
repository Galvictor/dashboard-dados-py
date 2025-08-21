import streamlit as st
import plotly.express as px

def display_product_analysis(df_filtered):
    """
    Exibe análise de produtos (top produtos por faturamento)
    """
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
