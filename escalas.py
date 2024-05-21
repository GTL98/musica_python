# --- Importar as bibliotecas --- #
from modos import *
from tabulate import tabulate


class Escalas:
    """
    Classe responsável por armazenar as escalas.
    """
    def __init__(self):
        """
        Função responsável por inicializar a classe.
        """

    def jonio(self, tom) -> str:
        """
        Escala responsável por retornar as escalas do tom no modo Jônio (maior).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = jonio[tom]
        except KeyError:
            return 'O tom não foi selecionado.'

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Criar o dicionário que originará a tabela --- #
            graus = [[I, II, III, IV, V, VI, VII]]

            # --- Transformar a lista em tabela --- #
            tabela = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela

    def dorico(self, tom) -> str:
        """
        Escala responsável por retornar as escalas do tom no modo Dórico (menor).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = dorico[tom]
        except KeyError:
            return 'O tom não foi selecionado.'

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Criar o dicionário que originará a tabela --- #
            graus = [[I, II, III, IV, V, VI, VII]]

            # --- Transformar a lista em tabela --- #
            tabela = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela
