# Chatbot de Predição de Churn

Aplicação interativa desenvolvida em **Python e Streamlit** para consulta de resultados de **predição de churn** utilizando um **UUID** como identificador único.  
Os dados são carregados a partir de um dataset estruturado em **JSON**, originado de uma base Excel.

---

## 📌 Visão Geral

Este projeto demonstra um fluxo típico de **Data Science / Engenharia de Dados**, integrando:

- Armazenamento de dados estruturados
- Consulta por identificador único (UUID)
- Exibição de resultados preditivos
- Interface simples e interativa via Streamlit

---

## 🚀 Funcionalidades

- Consulta de clientes via UUID
- Exibição de:
  - Probabilidade de Churn
  - Predição Final
  - Classificação de Risco
  - Modelo utilizado
  - Threshold aplicado
  - Data da predição
- Tratamento de cliente não encontrado
- Dataset padronizado e escalável

---

## 🗂 Estrutura do Projeto

chatbot_churn_uuid/
├── app.py
├── logic.py
├── dataset.json
├── requirements.txt
└── README.md


---

## 🛠 Tecnologias

- Python 3
- Streamlit
- Pandas
- JSON
- Excel (origem dos dados)
- UUID

---

## ▶️ Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
Execute a aplicação:
streamlit run app.py
Como Usar
uuid=<seu_uuid>
🎯 Objetivo

Este projeto pode ser utilizado como:

Portfólio em Data Science

Demonstração de consulta preditiva

Base para sistemas de churn em produção

Prova de conceito para aplicações analíticas

🔮 Melhorias Futuras

Integração com modelo de Machine Learning real

Persistência em banco de dados

Criação de API REST

Deploy em cloud

Autenticação de usuári
