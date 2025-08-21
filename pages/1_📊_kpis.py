import streamlit as st
from modules.kpis import display_main_kpis
from utils.sidebar_filters import create_global_sidebar

# Configuração da página
st.set_page_config(page_title="KPIs", page_icon="📊", layout="wide")

# Criar sidebar global com filtros
df_filtered = create_global_sidebar()

# Título da página
st.title("📊 KPIs Principais")

# Obter filtros da sessão para exibir
filters = st.session_state['filters']
st.markdown(f"**Período:** {filters['month']} | **Cidades:** {', '.join(filters['city_filter'])} | **Produtos:** {', '.join(filters['product_filter'])}")

# Descrição
st.markdown("""
Esta página mostra os principais indicadores de performance (KPIs) do negócio.
Os dados são filtrados automaticamente conforme as configurações da página principal.
""")

# Exibir KPIs
display_main_kpis(df_filtered)
