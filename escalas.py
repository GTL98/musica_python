# --- Importar as bibliotecas --- #
from typing import Tuple
from modos_gregos import *
from tabulate import tabulate


class ModosGregos:
    """
    Classe responsável por armazenar as escalas.
    """

    def jonio(self, tom) -> Tuple[str, str, str, str]:
        """
        Escala responsável por retornar as escalas do tom no modo Jônio (maior).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = jonio[tom]
        except KeyError:
            return 'O tom não foi selecionado.', '', '', ''

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Tabela com as notas --- #
            graus = [[I, II, III, IV, V, VI, VII]]
            tabela_graus = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com a disposição dos acordes --- #
            disposicao = [['Maior', 'Menor', 'Menor', 'Maior', 'Maior', 'Menor', 'Meio-diminuto']]
            tabela_disposicao = tabulate(
                tabular_data=disposicao,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com separação das notas --- #
            intervalos = [['T', 'T', 'sT', 'T', 'T', 'T', 'sT']]
            tabela_intervalos = tabulate(
                tabular_data=intervalos,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com os acordes --- #
            acordes = [[f'{I}', f'{II}m', f'{III}m', f'{IV}', f'{V}', f'{VI}m', f'{VII}m7(b5)']]
            tabela_acordes = tabulate(
                tabular_data=acordes,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela_graus, tabela_disposicao, tabela_intervalos, tabela_acordes

    def dorico(self, tom) -> Tuple[str, str, str, str]:
        """
        Escala responsável por retornar as escalas do tom no modo Dórico (menor).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = dorico[tom]
        except KeyError:
            return 'O tom não foi selecionado.', '', '', ''

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Tabela com as notas --- #
            graus = [[I, II, III, IV, V, VI, VII]]
            tabela_graus = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com a disposição dos acordes --- #
            disposicao = [['Menor', 'Menor', 'Maior', 'Maior', 'Menor', 'Meio-diminuto', 'Maior']]
            tabela_disposicao = tabulate(
                tabular_data=disposicao,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com separação das notas --- #
            intervalos = [['T', 'sT', 'T', 'T', 'T', 'sT', 'T']]
            tabela_intervalos = tabulate(
                tabular_data=intervalos,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com os acordes --- #
            acordes = [[f'{I}m', f'{II}m', f'{III}', f'{IV}', f'{V}m', f'{VI}m7(b5)', f'{VII}']]
            tabela_acordes = tabulate(
                tabular_data=acordes,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela_graus, tabela_disposicao, tabela_intervalos, tabela_acordes

    def frigio(self, tom) -> Tuple[str, str, str, str]:
        """
        Escala responsável por retornar as escalas do tom no modo Frígio (menor).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = frigio[tom]
        except KeyError:
            return 'O tom não foi selecionado.', '', '', ''

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Tabela com as notas --- #
            graus = [[I, II, III, IV, V, VI, VII]]
            tabela_graus = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com a disposição dos acordes --- #
            disposicao = [['Menor', 'Maior', 'Maior', 'Menor', 'Meio-diminuto', 'Maior', 'Menor']]
            tabela_disposicao = tabulate(
                tabular_data=disposicao,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com separação das notas --- #
            intervalos = [['sT', 'T', 'T', 'T', 'sT', 'T', 'T']]
            tabela_intervalos = tabulate(
                tabular_data=intervalos,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com os acordes --- #
            acordes = [[f'{I}m', f'{II}', f'{III}', f'{IV}m', f'{V}m7(b5)', f'{VI}', f'{VII}m']]
            tabela_acordes = tabulate(
                tabular_data=acordes,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela_graus, tabela_disposicao, tabela_intervalos, tabela_acordes

    def lidio(self, tom) -> Tuple[str, str, str, str]:
        """
        Escala responsável por retornar as escalas do tom no modo Lídio (maior).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = lidio[tom]
        except KeyError:
            return 'O tom não foi selecionado.', '', '', ''

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Tabela com as notas --- #
            graus = [[I, II, III, IV, V, VI, VII]]
            tabela_graus = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com a disposição dos acordes --- #
            disposicao = [['Maior', 'Maior', 'Menor', 'Meio-diminuto', 'Maior', 'Menor', 'Menor']]
            tabela_disposicao = tabulate(
                tabular_data=disposicao,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com separação das notas --- #
            intervalos = [['T', 'T', 'T', 'sT', 'T', 'T', 'sT']]
            tabela_intervalos = tabulate(
                tabular_data=intervalos,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com os acordes --- #
            acordes = [[f'{I}', f'{II}', f'{III}m', f'{IV}m7(b5)', f'{V}', f'{VI}m', f'{VII}m']]
            tabela_acordes = tabulate(
                tabular_data=acordes,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela_graus, tabela_disposicao, tabela_intervalos, tabela_acordes

    def mixolidio(self, tom) -> Tuple[str, str, str, str]:
        """
        Escala responsável por retornar as escalas do tom no modo Mixolídio (maior).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = mixolidio[tom]
        except KeyError:
            return 'O tom não foi selecionado.', '', '', ''

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Tabela com as notas --- #
            graus = [[I, II, III, IV, V, VI, VII]]
            tabela_graus = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com a disposição dos acordes --- #
            disposicao = [['Maior', 'Menor', 'Meio-diminuto', 'Maior', 'Menor', 'Menor', 'Maior']]
            tabela_disposicao = tabulate(
                tabular_data=disposicao,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com separação das notas --- #
            intervalos = [['T', 'T', 'sT', 'T', 'T', 'sT', 'T']]
            tabela_intervalos = tabulate(
                tabular_data=intervalos,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com os acordes --- #
            acordes = [[f'{I}', f'{II}m', f'{III}m7(b5)', f'{IV}', f'{V}m', f'{VI}m', f'{VII}']]
            tabela_acordes = tabulate(
                tabular_data=acordes,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela_graus, tabela_disposicao, tabela_intervalos, tabela_acordes

    def eolio(self, tom) -> Tuple[str, str, str, str]:
        """
        Escala responsável por retornar as escalas do tom no modo Eólio (menor).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = eolio[tom]
        except KeyError:
            return 'O tom não foi selecionado.', '', '', ''

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Tabela com as notas --- #
            graus = [[I, II, III, IV, V, VI, VII]]
            tabela_graus = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com a disposição dos acordes --- #
            disposicao = [['Menor', 'Meio-diminuto', 'Maior', 'Menor', 'Menor', 'Maior', 'Maior']]
            tabela_disposicao = tabulate(
                tabular_data=disposicao,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com separação das notas --- #
            intervalos = [['T', 'sT', 'T', 'T', 'sT', 'T', 'T']]
            tabela_intervalos = tabulate(
                tabular_data=intervalos,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com os acordes --- #
            acordes = [[f'{I}m', f'{II}m7(b5)', f'{III}', f'{IV}m', f'{V}m', f'{VI}', f'{VII}']]
            tabela_acordes = tabulate(
                tabular_data=acordes,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela_graus, tabela_disposicao, tabela_intervalos, tabela_acordes

    def locrio(self, tom) -> Tuple[str, str, str, str]:
        """
        Escala responsável por retornar as escalas do tom no modo Lócrio (menor).
        :param tom: Tom da escala.
        :return: String de uma tabela das notas da escala.
        """
        # --- Tratar a informação --- #
        try:
            notas = locrio[tom]
        except KeyError:
            return 'O tom não foi selecionado.', '', '', ''

        else:
            # --- Separar os graus --- #
            I = notas[0]
            II = notas[1]
            III = notas[2]
            IV = notas[3]
            V = notas[4]
            VI = notas[5]
            VII = notas[6]

            # --- Tabela com as notas --- #
            graus = [[I, II, III, IV, V, VI, VII]]
            tabela_graus = tabulate(
                tabular_data=graus,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com a disposição dos acordes --- #
            disposicao = [['Meio-diminuto', 'Maior', 'Menor', 'Menor', 'Maior', 'Maior', 'Menor']]
            tabela_disposicao = tabulate(
                tabular_data=disposicao,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com separação das notas --- #
            intervalos = [['sT', 'T', 'T', 'sT', 'T', 'T', 'T']]
            tabela_intervalos = tabulate(
                tabular_data=intervalos,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            # --- Tabela com os acordes --- #
            acordes = [[f'{I}m7(b5)', f'{II}', f'{III}m', f'{IV}m', f'{V}', f'{VI}', f'{VII}m']]
            tabela_acordes = tabulate(
                tabular_data=acordes,
                headers=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
                tablefmt='html'
            )

            return tabela_graus, tabela_disposicao, tabela_intervalos, tabela_acordes