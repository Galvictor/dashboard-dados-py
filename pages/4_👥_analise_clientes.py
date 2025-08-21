import streamlit as st
from modules.customer_analysis import display_customer_analysis
from utils.sidebar_filters import create_global_sidebar

# Configuração da página
st.set_page_config(page_title="Análise de Clientes", page_icon="👥", layout="wide")

# Criar sidebar global com filtros
df_filtered = create_global_sidebar()

# Título da página
st.title("👥 Análise de Clientes")

# Obter filtros da sessão para exibir
filters = st.session_state['filters']
st.markdown(f"**Período:** {filters['month']} | **Cidades:** {', '.join(filters['city_filter'])} | **Produtos:** {', '.join(filters['product_filter'])}")

# Descrição
st.markdown("""
Esta página mostra a análise detalhada dos clientes, incluindo segmentação, comportamento de compra e preferências.
Os dados são filtrados automaticamente conforme as configurações da página principal.
""")

# Exibir análise de clientes
display_customer_analysis(df_filtered)
