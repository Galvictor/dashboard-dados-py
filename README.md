# 📊 Dashboard de Vendas - Supermercado

Um dashboard interativo criado com Streamlit para análise avançada de dados de vendas de supermercado, com estrutura modular e organizada.

## 🏗️ **Estrutura do Projeto**

```
dashboard_dados_py/
├── dashboard.py              # 🚀 Dashboard principal (modular e organizado)
├── modules/                  # 📦 Módulos de análise
│   ├── __init__.py
│   ├── kpis.py              # KPIs principais
│   ├── temporal_analysis.py # Análise temporal
│   ├── product_analysis.py  # Análise de produtos
│   ├── customer_analysis.py # Análise de clientes
│   ├── branch_analysis.py   # Análise de filiais
│   ├── margin_analysis.py   # Análise de margem
│   └── original_charts.py   # Gráficos originais
├── utils/                    # 🛠️ Utilitários
│   ├── __init__.py
│   └── data_loader.py       # Carregamento de dados
├── supermarket_sales.csv     # Dataset de vendas
├── TODO.md                   # Lista de tarefas e próximos passos
└── README.md                 # Este arquivo
```

## 🚀 **Tecnologias Utilizadas**

-   **Streamlit** - Framework para criação de aplicações web de dados
-   **Pandas** - Manipulação e análise de dados
-   **Plotly** - Criação de gráficos interativos
-   **Python 3.13** - Linguagem de programação

## 🛠️ **Instalação**

### Pré-requisitos

-   Python 3.8 ou superior
-   pip (gerenciador de pacotes Python)

### Passos para instalação

1. **Clone ou baixe o projeto**
2. **Navegue até a pasta do projeto**

    ```bash
    cd dashboard_dados_py
    ```

3. **Crie e ative o ambiente virtual**

    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\Activate.ps1

    # Linux/Mac
    python -m venv .venv
    source .venv/bin/activate
    ```

4. **Instale as dependências**
    ```bash
    pip install streamlit pandas plotly
    ```

## 🎯 **Como Executar**

1. **Ative o ambiente virtual** (se não estiver ativo)

    ```bash
    .venv\Scripts\Activate.ps1  # Windows
    ```

2. **Execute o dashboard**

    ```bash
    streamlit run dashboard.py
    ```

3. **Acesse no navegador**
    - O dashboard será aberto automaticamente em `http://localhost:8501`
    - Ou acesse manualmente a URL exibida no terminal

## ✨ **Vantagens da Estrutura Modular**

### 1. **🔧 Manutenibilidade**

-   Cada análise está em um arquivo separado
-   Fácil de encontrar e modificar funcionalidades específicas
-   Código mais limpo e organizado

### 2. **📈 Escalabilidade**

-   Adicionar novas análises é simples
-   Basta criar um novo módulo e importar no arquivo principal
-   Não afeta outras funcionalidades

### 3. **👥 Trabalho em Equipe**

-   Diferentes desenvolvedores podem trabalhar em módulos diferentes
-   Menos conflitos de merge
-   Código mais fácil de revisar

### 4. **🧪 Testabilidade**

-   Cada módulo pode ser testado independentemente
-   Mais fácil de debugar problemas específicos
-   Melhor isolamento de funcionalidades

## 📋 **Módulos Disponíveis**

### **🎯 KPIs (`modules/kpis.py`)**

-   Faturamento total
-   Ticket médio
-   Total de transações
-   Avaliação média

### **🕒 Análise Temporal (`modules/temporal_analysis.py`)**

-   Vendas por dia da semana
-   Vendas por hora do dia

### **🏆 Análise de Produtos (`modules/product_analysis.py`)**

-   Top produtos por faturamento
-   Ranking com porcentagens

### **👥 Análise de Clientes (`modules/customer_analysis.py`)**

-   Segmentação por tipo (Member vs Normal)
-   Análise por gênero
-   Distribuição de faturamento

### **🏢 Análise de Filiais (`modules/branch_analysis.py`)**

-   Performance por filial
-   Performance por cidade
-   Comparativo side-by-side

### **💰 Análise de Margem (`modules/margin_analysis.py`)**

-   Margem por linha de produto
-   Margem por cidade
-   Resumo financeiro

### **📊 Gráficos Originais (`modules/original_charts.py`)**

-   Faturamento por dia
-   Faturamento por tipo de produto
-   Faturamento por filial
-   Formas de pagamento
-   Avaliações

## 🆕 **Como Adicionar Novas Análises**

### 1. **Criar Novo Módulo**

```python
# modules/nova_analise.py
import streamlit as st
import plotly.express as px

def display_nova_analise(df_filtered):
    st.header("🆕 Nova Análise")
    # Sua análise aqui
    pass
```

### 2. **Importar no Arquivo Principal**

```python
# dashboard.py
from modules.nova_analise import display_nova_analise

# Adicionar na sequência
display_nova_analise(df_filtered)
```

## 📊 **Funcionalidades Implementadas**

### ✅ **Alta Prioridade (Concluídas)**

-   [x] Análise temporal avançada
-   [x] Top produtos por faturamento
-   [x] Segmentação de clientes
-   [x] Performance por filial
-   [x] Análise de margem

### 🔄 **Próximos Passos**

-   [ ] Análise de pagamentos
-   [ ] Correlações entre variáveis
-   [ ] KPIs dinâmicos avançados

## 📊 **Dataset**

O projeto utiliza o arquivo `supermarket_sales.csv` que contém dados de vendas de supermercado, incluindo:

-   **1000+ transações** de Janeiro a Março de 2019
-   **3 cidades**: Yangon, Mandalay, Naypyitaw
-   **3 filiais**: A, B, C
-   **6 linhas de produto**: Health & beauty, Electronic accessories, Home & lifestyle, Sports & travel, Fashion accessories, Food & beverages
-   **3 formas de pagamento**: Cash, Ewallet, Credit card
-   **2 tipos de cliente**: Member vs Normal
-   **Dados financeiros**: Preço unitário, quantidade, impostos, margem, COGS

## 🤝 **Contribuição**

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📝 **Licença**

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 **Suporte**

Para dúvidas ou suporte, entre em contato através das issues do repositório.

---

**🎉 Dashboard organizado, modular e fácil de expandir!**

**Desenvolvido com ❤️ usando Streamlit e Python**
