# 📊 Dashboard de Vendas - Supermercado

Um dashboard interativo e profissional criado com Streamlit para análise avançada de dados de vendas de supermercado, com estrutura modular, navegação por páginas e filtros globais.

## 🏗️ **Estrutura do Projeto**

```
dashboard_dados_py/
├── dashboard.py              # 🚀 Página principal com visão geral
├── pages/                    # 📄 Páginas específicas do Streamlit
│   ├── 1_📊_kpis.py         # KPIs principais
│   ├── 2_⏰_analise_temporal.py
│   ├── 3_📦_analise_produtos.py
│   ├── 4_👥_analise_clientes.py
│   ├── 5_🏪_analise_filiais.py
│   ├── 6_💰_analise_margem.py
│   └── 7_📊_graficos_originais.py
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
│   ├── data_loader.py       # Carregamento de dados
│   └── sidebar_filters.py   # Filtros globais da sidebar
├── supermarket_sales.csv     # Dataset de vendas
├── TODO.md                   # Lista de tarefas e próximos passos
└── README.md                 # Este arquivo
```

## 🚀 **Tecnologias Utilizadas**

-   **Streamlit** - Framework para criação de aplicações web de dados
-   **Streamlit Pages** - Sistema de navegação por páginas
-   **Pandas** - Manipulação e análise de dados
-   **Plotly** - Criação de gráficos interativos
-   **Python 3.13** - Linguagem de programação

## 🆕 **Novidades da Versão 2.0**

### ✨ **Sistema de Páginas**

-   **Navegação intuitiva** entre diferentes análises
-   **Páginas específicas** para cada tipo de análise
-   **Menu lateral automático** criado pelo Streamlit
-   **URLs únicas** para cada página

### 🔄 **Filtros Globais**

-   **Sidebar persistente** em todas as páginas
-   **Filtros sincronizados** entre páginas
-   **Dados compartilhados** via session state
-   **Performance otimizada** com cache inteligente

### 📱 **Experiência do Usuário**

-   **Interface responsiva** e moderna
-   **Navegação fluida** entre análises
-   **Foco específico** em cada página
-   **Carregamento rápido** de conteúdo

## 🛠️ **Instalação**

### Pré-requisitos

-   Python 3.8 ou superior
-   pip (gerenciador de pacotes Python)

### **Opção 1: Instalação rápida (recomendada)**

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
    pip install -r requirements.txt
    ```

### **Opção 2: Instalação com dependências de desenvolvimento**

```bash
pip install -r requirements-dev.txt
```

### **Opção 3: Instalação manual**

```bash
pip install streamlit>=1.28.0 pandas>=2.0.0 plotly>=5.15.0 numpy>=1.24.0
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

## 🧭 **Navegação e Páginas**

### **🏠 Página Principal (`dashboard.py`)**

-   **Visão geral completa** de todas as análises
-   **Filtros globais** na sidebar
-   **KPIs principais** em destaque
-   **Resumo executivo** do negócio

### **📊 Páginas Específicas**

-   **1_📊_kpis.py** - Indicadores de performance detalhados
-   **2_⏰_analise_temporal.py** - Análise de tendências e sazonalidade
-   **3_📦_analise_produtos.py** - Performance e ranking de produtos
-   **4_👥_analise_clientes.py** - Segmentação e comportamento de clientes
-   **5_🏪_analise_filiais.py** - Performance por localização
-   **6_💰_analise_margem.py** - Análise de rentabilidade
-   **7_📊_graficos_originais.py** - Visualizações complementares

## ✨ **Vantagens da Nova Estrutura**

### 1. **🔧 Manutenibilidade**

-   Cada análise está em uma página separada
-   Fácil de encontrar e modificar funcionalidades específicas
-   Código mais limpo e organizado

### 2. **📈 Escalabilidade**

-   Adicionar novas páginas é simples
-   Basta criar um novo arquivo na pasta `pages/`
-   Navegação automática criada pelo Streamlit

### 3. **👥 Trabalho em Equipe**

-   Diferentes desenvolvedores podem trabalhar em páginas diferentes
-   Menos conflitos de merge
-   Código mais fácil de revisar

### 4. **🧪 Testabilidade**

-   Cada página pode ser testada independentemente
-   Mais fácil de debugar problemas específicos
-   Melhor isolamento de funcionalidades

### 5. **🎯 Foco do Usuário**

-   Cada página tem um objetivo específico
-   Não precisa fazer scroll infinito
-   Navegação intuitiva e rápida

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

## 🆕 **Como Adicionar Novas Páginas**

### 1. **Criar Nova Página**

```python
# pages/8_🆕_nova_analise.py
import streamlit as st
from modules.nova_analise import display_nova_analise
from utils.sidebar_filters import create_global_sidebar

# Configuração da página
st.set_page_config(page_title="Nova Análise", page_icon="🆕", layout="wide")

# Criar sidebar global com filtros
df_filtered = create_global_sidebar()

# Título da página
st.title("🆕 Nova Análise")

# Exibir análise
display_nova_analise(df_filtered)
```

### 2. **Criar Módulo Correspondente**

```python
# modules/nova_analise.py
import streamlit as st
import plotly.express as px

def display_nova_analise(df_filtered):
    st.header("🆕 Nova Análise")
    # Sua análise aqui
    pass
```

## 📊 **Funcionalidades Implementadas**

### ✅ **Alta Prioridade (Concluídas)**

-   [x] Sistema de páginas com Streamlit Pages
-   [x] Filtros globais persistentes
-   [x] Navegação intuitiva entre análises
-   [x] Análise temporal avançada
-   [x] Top produtos por faturamento
-   [x] Segmentação de clientes
-   [x] Performance por filial
-   [x] Análise de margem
-   [x] Sidebar global funcional

### 🔄 **Próximos Passos**

-   [ ] Análise de pagamentos
-   [ ] Correlações entre variáveis
-   [ ] KPIs dinâmicos avançados
-   [ ] Exportação de relatórios
-   [ ] Temas personalizáveis

## 📊 **Dataset**

O projeto utiliza o arquivo `supermarket_sales.csv` que contém dados de vendas de supermercado, incluindo:

-   **1000+ transações** de Janeiro a Março de 2019
-   **3 cidades**: Yangon, Mandalay, Naypyitaw
-   **3 filiais**: A, B, C
-   **6 linhas de produto**: Health & beauty, Electronic accessories, Home & lifestyle, Sports & travel, Fashion accessories, Food & beverages
-   **3 formas de pagamento**: Cash, Ewallet, Credit card
-   **2 tipos de cliente**: Member vs Normal
-   **Dados financeiros**: Preço unitário, quantidade, impostos, margem, COGS

## 🎨 **Interface e UX**

### **Design Responsivo**

-   Layout adaptável para diferentes dispositivos
-   Sidebar sempre visível com filtros
-   Navegação clara e intuitiva

### **Filtros Inteligentes**

-   Filtros por período, cidade e produto
-   Aplicação automática em todas as páginas
-   Persistência entre navegações

### **Visualizações Interativas**

-   Gráficos Plotly responsivos
-   Hover effects informativos
-   Zoom e pan em gráficos complexos

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

**🎉 Dashboard profissional com navegação por páginas e filtros globais!**

**Desenvolvido com ❤️ usando Streamlit, Python e Streamlit Pages**

**Versão 2.0 - Sistema de Páginas e Filtros Globais**
