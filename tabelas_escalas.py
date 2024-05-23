# --- Importar as bibliotecas --- #
import streamlit as st
from typing import Tuple


def tabelas_modos_gregos(escala: Tuple[str, str, str, str], modo: str, tom: str) -> None:
    """
    Função responsável por criar o layout da página com as tabelas.
    :param escala: Modo Grego escolhido.
    :param modo: Qual Modo Grrego foi selecionado.
    :param tom: Qual tom da escala foi selecionado.
    """

    # --- Separar as tabelas --- #
    escala_notas = escala[0]
    escala_disposicao = escala[1]
    escala_intervalo = escala[2]
    escala_acordes = escala[3]

    # --- Mostrar a tabela das notas --- #
    st.subheader(f'Notas da escala do tom: :green[{tom}]')
    st.write(escala_notas, unsafe_allow_html=True)
    st.write('---')

    # --- Mostrar a tabela da disposição dos acordes --- #
    st.subheader(f'Disposição dos acordes do modo: :green[{modo}]')
    st.write(escala_disposicao, unsafe_allow_html=True)
    st.write('---')

    # --- Mostrar a tabela com os intervalos --- #
    st.subheader(f'Intervalos do modo: :green[{modo}]')
    st.write(escala_intervalo, unsafe_allow_html=True)
    st.write('---')

    # --- Mostrar a tabela dos acordes --- #
    st.subheader(f'Acordes do modo: :green[{modo}]')
    st.write(escala_acordes, unsafe_allow_html=True)
