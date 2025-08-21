import pandas as pd
import streamlit as st

def load_and_prepare_data():
    """
    Carrega e prepara os dados do CSV para análise
    """
    # Carregar dados
    df = pd.read_csv("supermarket_sales.csv", sep=",", decimal=",")
    
    # Converter colunas numéricas
    numeric_columns = [
        "Total", "Rating", "gross income", "Tax 5%", 
        "cogs", "Unit price", "Quantity", "gross margin percentage"
    ]
    
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Converter data
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    
    # Adicionar colunas temporais
    df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
    df["DayOfWeek"] = df["Date"].dt.day_name()
    df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour
    
    return df

def apply_filters(df, month, city_filter, product_filter):
    """
    Aplica filtros aos dados
    """
    return df[
        (df["Month"] == month) & 
        (df["City"].isin(city_filter)) & 
        (df["Product line"].isin(product_filter))
    ]

def create_sidebar_filters(df):
    """
    Cria os filtros na sidebar
    """
    st.sidebar.header("📊 Filtros")
    
    month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique())
    city_filter = st.sidebar.multiselect(
        "Selecione as cidades", 
        df["City"].unique(), 
        default=df["City"].unique()
    )
    product_filter = st.sidebar.multiselect(
        "Selecione as linhas de produto", 
        df["Product line"].unique(), 
        default=df["Product line"].unique()
    )
    
    return month, city_filter, product_filter
