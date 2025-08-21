# Dashboard de Dados - Supermercado

Um dashboard interativo criado com Streamlit para análise de dados de vendas de supermercado.

## 📊 Descrição

Este projeto apresenta um dashboard web interativo que permite visualizar e analisar dados de vendas de supermercado de forma dinâmica e responsiva.

## 🚀 Tecnologias Utilizadas

-   **Streamlit** - Framework para criação de aplicações web de dados
-   **Pandas** - Manipulação e análise de dados
-   **Plotly** - Criação de gráficos interativos
-   **Python 3.13** - Linguagem de programação

## 📁 Estrutura do Projeto

```
dashboard_dados_py/
├── dashboard.py              # Arquivo principal do dashboard
├── supermarket_sales.csv     # Dataset de vendas do supermercado
├── .venv/                    # Ambiente virtual Python
└── README.md                 # Este arquivo
```

## 🛠️ Instalação

### Pré-requisitos

-   Python 3.13 ou superior
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

## 🎯 Como Executar

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

## 📈 Funcionalidades

-   **Visualização de dados** - Análise interativa das vendas
-   **Gráficos dinâmicos** - Criação de visualizações com Plotly
-   **Interface responsiva** - Dashboard adaptável a diferentes dispositivos
-   **Análise em tempo real** - Processamento dinâmico dos dados

## 📊 Dataset

O projeto utiliza o arquivo `supermarket_sales.csv` que contém dados de vendas de supermercado, incluindo:

-   Informações de produtos
-   Dados de vendas
-   Métricas de performance
-   Dados temporais

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Para dúvidas ou suporte, entre em contato através das issues do repositório.

---

**Desenvolvido com ❤️ usando Streamlit e Python**
