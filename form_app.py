# form_app.py

import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Formulário de Observação", layout="centered")

st.title("📝 Formulário de Observação de Segurança")

# === DADOS GERAIS ===
email = st.text_input("E-mail")
observador = st.selectbox("Observador", ["Bruno", "Jonan", "Fabiane"])
avaliacao = st.selectbox("Avaliação", ["1", "2", "3", "4"])
setor = st.selectbox("Setor", [
    "Fôrmas",
    "Armação",
    "Desforma",
    "Corte Solda",
    "Concretagem",
    "Movimentação",
    "Estocagem",
    "Controle de Qualidade",
    "Manutenção",
    "Administrativo",
    "Limpeza",
    "Outros"
])

uploaded_file = st.file_uploader("Upload de Foto ou Arquivo", type=["png", "jpg", "jpeg", "pdf"])

# === A. POSIÇÃO DAS PESSOAS ===
st.header("A. Posição das Pessoas")
posicoes = {
    "Postura correta na atividade": 0,
    "Manutenção de distância segura de equipamentos": 0,
    "Trabalho em altura com segurança": 0,
    "Afastamento de áreas de risco": 0,
    "Utilização correta de ferramentas": 0,
}
for item in posicoes:
    posicoes[item] = st.selectbox(item, [0.0, 0.1, 0.2, 0.3], key=item)

# === B. EPIs ===
st.header("B. EPIs")
epis = {
    "Capacete": 0,
    "Óculos de proteção": 0,
    "Luvas": 0,
    "Protetor auricular": 0,
    "Botina": 0,
    "Colete": 0,
}
for item in epis:
    epis[item] = st.selectbox(item, [0.0, 0.75], key=item)

# === C. ARRUMAÇÃO E LIMPEZA ===
st.header("C. Arrumação e Limpeza")
limpeza = {
    "Local de trabalho limpo": 0,
    "Organização de ferramentas": 0,
    "Sinalização adequada": 0,
    "Descarte correto de resíduos": 0,
}
for item in limpeza:
    limpeza[item] = st.selectbox(item, [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], key=item)

# === BOTÃO DE SALVAR ===
if st.button("Salvar Dados"):
    dados = {
        "Data/Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "E-mail": email,
        "Observador": observador,
        "Avaliação": avaliacao,
        "Setor": setor,
    }

    # Notas
    for k, v in posicoes.items():
        dados[f"A: {k}"] = v
    for k, v in epis.items():
        dados[f"B: {k}"] = v
    for k, v in limpeza.items():
        dados[f"C: {k}"] = v

    # Salvar em Excel
    df = pd.DataFrame([dados])
    excel_path = "dados_observacoes.xlsx"
    if os.path.exists(excel_path):
        df_existente = pd.read_excel(excel_path)
        df_total = pd.concat([df_existente, df], ignore_index=True)
    else:
        df_total = df
    df_total.to_excel(excel_path, index=False)

    st.success("✅ Dados salvos com sucesso!")
