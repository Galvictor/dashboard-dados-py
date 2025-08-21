import streamlit as st
from modules.temporal_analysis import display_temporal_analysis
from utils.sidebar_filters import create_global_sidebar

# Configuração da página
st.set_page_config(page_title="Análise Temporal", page_icon="⏰", layout="wide")

# Criar sidebar global com filtros
df_filtered = create_global_sidebar()

# Título da página
st.title("⏰ Análise Temporal")

# Obter filtros da sessão para exibir
filters = st.session_state['filters']
st.markdown(f"**Período:** {filters['month']} | **Cidades:** {', '.join(filters['city_filter'])} | **Produtos:** {', '.join(filters['product_filter'])}")

# Descrição
st.markdown("""
Esta página mostra a análise temporal das vendas, incluindo tendências, sazonalidade e padrões ao longo do tempo.
Os dados são filtrados automaticamente conforme as configurações da página principal.
""")

# Exibir análise temporal
display_temporal_analysis(df_filtered)
