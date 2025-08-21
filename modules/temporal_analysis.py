import streamlit as st
import plotly.express as px

def display_temporal_analysis(df_filtered):
    """
    Exibe análise temporal avançada (dias da semana e horários)
    """
    st.header("🕒 Análise Temporal")
    
    col1, col2 = st.columns(2)
    
    # Gráfico de vendas por dia da semana
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
