# --- Importar as bibliotecas --- #
import streamlit as st
from escalas import Pentatonicas
from tabelas_escalas import tabela_pentatonica

# --- Configurações da página --- #
st.set_page_config(page_title='Pentatônica', layout='centered')

# --- Configuração da tabela --- #
st.write(
    '''
    <style>
    table, th, td {
        font-size: 30px;
        }
    </style>
    ''', unsafe_allow_html=True
)

# --- Adicionar o título na página --- #
st.title('Pentatônica')

# --- Lista com os modos da pentatônica --- #
modos = [
    'Maior',
    'Menor'
]

# --- Caixa de seleção dos modos gregos --- #
modo = st.selectbox(
    label='Escolha uma opção',
    options=modos,
    placeholder='Selecione uma Pentatônica',
    index=None
)

# --- Lista com os tons --- #
tons = [
    'C',
    'C#/Db',
    'D',
    'D#/Eb',
    'E',
    'F',
    'F#/Gb',
    'G',
    'G#/Ab',
    'A',
    'A#/Bb',
    'B'
]

# --- Verificar se a caixa dos modos foi selecionada --- #
tom = None
if modo is not None:
    # --- Caixa de seleção das notas --- #
    tom = st.selectbox(
        label='Escolha uma opção',
        options=tons,
        placeholder='Selecione um tom',
        index=None
    )
    # --- Inicializar a classe --- #
    escala = Pentatonicas()

    # --- Mostrar a escala --- #
    if tom is not None:
        if modo == 'Maior':
            tabela_pentatonica(escala.maior(tom), modo, tom)

        elif modo == 'Menor':
            tabela_pentatonica(escala.menor(tom), modo, tom)
