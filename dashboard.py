import streamlit as st

# Importar módulos
from utils.sidebar_filters import create_global_sidebar
from modules.kpis import display_main_kpis
from modules.temporal_analysis import display_temporal_analysis
from modules.product_analysis import display_product_analysis
from modules.customer_analysis import display_customer_analysis
from modules.branch_analysis import display_branch_analysis
from modules.margin_analysis import display_margin_analysis
from modules.original_charts import display_original_charts

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas", page_icon="📊", layout="wide")

# Criar sidebar global com filtros
df_filtered = create_global_sidebar()

# Título principal
st.title("📊 Dashboard de Vendas - Supermercado")

# Obter filtros da sessão para exibir
filters = st.session_state['filters']
st.markdown(f"**Período:** {filters['month']} | **Cidades:** {', '.join(filters['city_filter'])} | **Produtos:** {', '.join(filters['product_filter'])}")

# Descrição da página
st.markdown("""
Esta é a página principal do dashboard. Use os filtros na barra lateral para ajustar os dados.
Navegue pelas outras páginas para análises específicas.
""")

# Exibir KPIs principais
st.header("📈 KPIs Principais")
display_main_kpis(df_filtered)

# Exibir análise temporal
st.header("⏰ Análise Temporal")
display_temporal_analysis(df_filtered)

# Exibir análise de produtos
st.header("📦 Análise de Produtos")
display_product_analysis(df_filtered)

# Exibir análise de clientes
st.header("👥 Análise de Clientes")
display_customer_analysis(df_filtered)

# Exibir análise de filiais
st.header("🏪 Análise de Filiais")
display_branch_analysis(df_filtered)

# Exibir análise de margem
st.header("💰 Análise de Margem")
display_margin_analysis(df_filtered)

# Exibir gráficos originais
st.header("📊 Gráficos Originais")
display_original_charts(df_filtered)
