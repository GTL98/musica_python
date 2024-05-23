# --- Importar as bibliotecas --- #
import streamlit as st
from escalas import ModosGregos
from tabelas_escalas import tabelas_modos_gregos

# --- Configurações da página --- #
st.set_page_config(page_title='Modos Gregos', layout='centered')

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
st.title('Modos Gregos')
st.write('---')

# --- Lista com os modos gregos --- #
modos = [
    'Jônio',
    'Dórico',
    'Frígio',
    'Lídio',
    'Mixolídio',
    'Eólio',
    'Lócrio'
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
    escala = ModosGregos()

    # --- Mostrar a escala --- #
    if tom is not None:
        if modo == 'Jônio':
            tabelas_modos_gregos(escala.jonio(tom), modo, tom)

        elif modo == 'Dórico':
            tabelas_modos_gregos(escala.dorico(tom), modo, tom)

        elif modo == 'Frígio':
            tabelas_modos_gregos(escala.frigio(tom), modo, tom)

        elif modo == 'Lídio':
            tabelas_modos_gregos(escala.lidio(tom), modo, tom)

        elif modo == 'Mixolídio':
            tabelas_modos_gregos(escala.mixolidio(tom), modo, tom)

        elif modo == 'Eólio':
            tabelas_modos_gregos(escala.eolio(tom), modo, tom)

        elif modo == 'Lócrio':
            tabelas_modos_gregos(escala.locrio(tom), modo, tom)
