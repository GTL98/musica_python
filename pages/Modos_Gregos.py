# --- Importar as bibliotecas --- #
import streamlit as st
from escalas import Escalas

# --- Configurações da página --- #
st.set_page_config(page_title='Modos Gregos', layout='centered')

# --- Configuração da tabela --- #
st.write(
    '''
    <style>
    table, th, td {
        font-size: 50px;
        }
    </style>
    ''', unsafe_allow_html=True
)

# --- Adicionar o título na página --- #
st.title('Modos Gregos')
st.write('---')

# --- Lista com os modos gregos --- #
modos = [
    'Jônio',
    'Dórico'
]

# --- Caixa de seleção dos modos gregos --- #
modo = st.selectbox(
    label='Escolha uma opção',
    options=modos,
    placeholder='Selecione um Modo Grego',
    index=None
)

# --- Lista com os tons --- #
tons = [
    'C',
    'C#',
    'D',
    'Eb',
    'E',
    'F',
    'F#',
    'G',
    'G#',
    'A',
    'Bb',
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
    escala = Escalas()

    # --- Mostrar a escala --- #
    if modo == 'Jônio':
        st.write(escala.jonio(tom), unsafe_allow_html=True)
