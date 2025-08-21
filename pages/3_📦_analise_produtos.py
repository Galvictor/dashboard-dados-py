import streamlit as st
from modules.product_analysis import display_product_analysis
from utils.sidebar_filters import create_global_sidebar

# Configuração da página
st.set_page_config(page_title="Análise de Produtos", page_icon="📦", layout="wide")

# Criar sidebar global com filtros
df_filtered = create_global_sidebar()

# Título da página
st.title("📦 Análise de Produtos")

# Obter filtros da sessão para exibir
filters = st.session_state['filters']
st.markdown(f"**Período:** {filters['month']} | **Cidades:** {', '.join(filters['city_filter'])} | **Produtos:** {', '.join(filters['product_filter'])}")

# Descrição
st.markdown("""
Esta página mostra a análise detalhada dos produtos, incluindo performance de vendas, categorias e tendências.
Os dados são filtrados automaticamente conforme as configurações da página principal.
""")

# Exibir análise de produtos
display_product_analysis(df_filtered)
