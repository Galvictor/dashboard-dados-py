import streamlit as st

def display_main_kpis(df_filtered):
    """
    Exibe os KPIs principais do dashboard
    """
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
