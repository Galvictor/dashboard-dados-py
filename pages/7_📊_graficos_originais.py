import streamlit as st
from modules.original_charts import display_original_charts
from utils.sidebar_filters import create_global_sidebar

# Configuração da página
st.set_page_config(page_title="Gráficos Originais", page_icon="📊", layout="wide")

# Criar sidebar global com filtros
df_filtered = create_global_sidebar()

# Título da página
st.title("📊 Gráficos Originais")

# Obter filtros da sessão para exibir
filters = st.session_state['filters']
st.markdown(f"**Período:** {filters['month']} | **Cidades:** {', '.join(filters['city_filter'])} | **Produtos:** {', '.join(filters['product_filter'])}")

# Descrição
st.markdown("""
Esta página mostra os gráficos originais do dataset, incluindo visualizações complementares e análises adicionais.
Os dados são filtrados automaticamente conforme as configurações da página principal.
""")

# Exibir gráficos originais
display_original_charts(df_filtered)
