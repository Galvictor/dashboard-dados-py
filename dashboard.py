import streamlit as st

# Importar módulos
from utils.data_loader import load_and_prepare_data, create_sidebar_filters, apply_filters
from modules.kpis import display_main_kpis
from modules.temporal_analysis import display_temporal_analysis
from modules.product_analysis import display_product_analysis
from modules.customer_analysis import display_customer_analysis
from modules.branch_analysis import display_branch_analysis
from modules.margin_analysis import display_margin_analysis
from modules.original_charts import display_original_charts

# Configuração da página
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# Carregar e preparar dados
df = load_and_prepare_data()

# Criar filtros na sidebar
month, city_filter, product_filter = create_sidebar_filters(df)

# Aplicar filtros
df_filtered = apply_filters(df, month, city_filter, product_filter)

# Título principal
st.title("📈 Dashboard de Vendas - Supermercado")
st.markdown(f"**Período:** {month} | **Cidades:** {', '.join(city_filter)} | **Produtos:** {', '.join(product_filter)}")

# Exibir todas as análises
display_main_kpis(df_filtered)
display_temporal_analysis(df_filtered)
display_product_analysis(df_filtered)
display_customer_analysis(df_filtered)
display_branch_analysis(df_filtered)
display_margin_analysis(df_filtered)
display_original_charts(df_filtered)
