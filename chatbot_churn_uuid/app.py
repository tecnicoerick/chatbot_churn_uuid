import streamlit as st
from logic import consultar_cliente_por_uuid

st.set_page_config(page_title="Chatbot de Predição de Churn")

st.title("Chatbot de Predição de Churn")
st.write("Digite no formato: `uuid=<valor>`")

# Inicializa estado
if "resultado" not in st.session_state:
    st.session_state.resultado = None

entrada = st.text_input("Consulta", placeholder="uuid=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

if st.button("Consultar"):
    st.session_state.resultado = consultar_cliente_por_uuid(entrada)

# Renderização CONTROLADA (evita erro removeChild)
if st.session_state.resultado:
    resultado = st.session_state.resultado

    if "erro" in resultado:
        st.error(resultado["erro"])
    else:
        st.success(resultado["status"])

        st.markdown("### Resultado da Predição")

        st.write(f"**UUID:** {resultado['UUID']}")
        st.write(f"**Probabilidade de Churn:** {resultado['Probabilidade de Churn']}")
        st.write(f"**Predição Final:** {resultado['Predição Final']}")
        st.write(f"**Classificação de Risco:** {resultado['Classificação de Risco']}")
        st.write(f"**Modelo utilizado:** {resultado['Modelo utilizado']}")
        st.write(f"**Threshold aplicado:** {resultado['Threshold aplicado']}")
        st.write(f"**Data da predição:** {resultado['Data da predição']}")
