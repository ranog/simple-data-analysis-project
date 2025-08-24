import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="PI4 — Dashboard (CSV ou API)", layout="centered")
st.title("PI4 — Dashboard Simples (CSV local OU API pública)")
st.write("""
Este app permite carregar dados de **duas formas**:
1) **CSV local** em `data/` (ex.: `cancer_example.csv`)
2) **API pública** que retorne JSON em lista de objetos com pelo menos `year` e `cases`.
""")


# -----------------------------
# Funções auxiliares
# -----------------------------
@st.cache_data
def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


@st.cache_data
def load_api_json(url: str) -> pd.DataFrame:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()
    if isinstance(data, dict):
        for v in data.values():
            if isinstance(v, list):
                data = v
                break
    return pd.DataFrame(data)


# -----------------------------
# Escolha da fonte
# -----------------------------
fonte = st.radio("Fonte de dados", ["CSV local", "API pública (JSON)"])
if fonte == "CSV local":
    path = st.text_input("CSV path", "src/data/cancer_example.csv")
    if st.button("Carregar CSV"):
        df = load_csv(path)
    else:
        df = None
else:
    url = st.text_input("API URL", "")
    if st.button("Chamar API"):
        df = load_api_json(url)
    else:
        df = None
# -----------------------------
# Exibição e modelo
# -----------------------------
if df is not None:
    st.subheader("Prévia dos dados")
    st.dataframe(df.head())
    if "year" in df.columns and "cases" in df.columns:
        st.subheader("Gráfico de evolução")
        fig, ax = plt.subplots()
        ax.plot(df["year"], df["cases"], marker="o")
        ax.set_xlabel("Ano")
        ax.set_ylabel("Casos")
        st.pyplot(fig)
        # Modelo simples
        st.subheader("Previsão (Regressão Linear)")
        model = LinearRegression().fit(df[["year"]], df["cases"])
        ano_pred = st.number_input(
            "Ano para prever", min_value=int(df["year"].max()) + 1, value=int(df["year"].max()) + 1
        )
        pred = model.predict([[ano_pred]])[0]
        st.write(f"**Previsão de casos para {ano_pred}: {pred:.0f}**")
    else:
        st.warning("O dataset precisa ter colunas 'year' e 'cases'.")
