import streamlit as st
from utils.data_loader import load_and_prepare_data, create_sidebar_filters, apply_filters

def create_global_sidebar():
    """
    Cria a sidebar global com filtros que funcionam em todas as páginas
    """
    # Carregar dados apenas uma vez
    if 'df' not in st.session_state:
        st.session_state['df'] = load_and_prepare_data()
    
    # Criar filtros na sidebar
    month, city_filter, product_filter = create_sidebar_filters(st.session_state['df'])
    
    # Aplicar filtros
    df_filtered = apply_filters(st.session_state['df'], month, city_filter, product_filter)
    
    # Armazenar dados filtrados na sessão
    st.session_state['df_filtered'] = df_filtered
    st.session_state['filters'] = {
        'month': month,
        'city_filter': city_filter,
        'product_filter': product_filter
    }
    
    return df_filtered

def get_filtered_data():
    """
    Retorna os dados filtrados da sessão ou cria novos se necessário
    """
    if 'df_filtered' in st.session_state:
        return st.session_state['df_filtered']
    else:
        return create_global_sidebar()
