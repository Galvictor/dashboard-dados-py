import streamlit as st
from modules.branch_analysis import display_branch_analysis
from utils.sidebar_filters import create_global_sidebar

# Configuração da página
st.set_page_config(page_title="Análise de Filiais", page_icon="🏪", layout="wide")

# Criar sidebar global com filtros
df_filtered = create_global_sidebar()

# Título da página
st.title("🏪 Análise de Filiais")

# Obter filtros da sessão para exibir
filters = st.session_state['filters']
st.markdown(f"**Período:** {filters['month']} | **Cidades:** {', '.join(filters['city_filter'])} | **Produtos:** {', '.join(filters['product_filter'])}")

# Descrição
st.markdown("""
Esta página mostra a análise detalhada das filiais, incluindo performance por localização e comparações entre unidades.
Os dados são filtrados automaticamente conforme as configurações da página principal.
""")

# Exibir análise de filiais
display_branch_analysis(df_filtered)
