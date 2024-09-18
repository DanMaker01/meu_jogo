import re
from typing import Any

class Roteiro:
    def __init__(self, nome_arquivo_roteiro='roteiro1.txt'):
        # print("Iniciou classe Roteiro")
        self.local = ""
        self.roteiro_organizado = []
        self.gerar_roteiro(nome_arquivo_roteiro)

    def get_endereco_completo(self, nome_arquivo: str) -> str:
        return self.local + nome_arquivo

    def importar_arquivo(self, nome_arquivo: str) -> str:
        endereco_completo = self.get_endereco_completo(nome_arquivo)
        with open(endereco_completo, 'r', encoding='utf-8') as file:
            return file.read()

    def processar_texto(self, texto_importado_bruto: str) -> list:
        if not texto_importado_bruto:
            print("erro ao processar o texto")
            return []
        
        linhas = texto_importado_bruto.strip().split('\n')
        resultado = []

        for linha in linhas:
            partes = linha.split('@')
            nome, texto = partes[0], partes[1]
            opcoes = []

            for opcao in partes[2:]:
                opcao_valor_condicao = opcao.split('#')
                opcao_nome = opcao_valor_condicao[0]
                valor = int(opcao_valor_condicao[1])
                condicao = None
                
                if len(opcao_valor_condicao) == 3:
                    condicao_completa = opcao_valor_condicao[2]
                    padrao_condicao = r"([a-zA-Z_]+)([><=!]+)(\d+\.?\d*)"
                    match = re.match(padrao_condicao, condicao_completa)
                    if match:
                        condicao = [match.group(1), match.group(2), float(match.group(3))]
                
                opcoes.append([opcao_nome, valor, condicao])

            resultado.append([nome, texto, opcoes])

        return resultado

    def gerar_roteiro(self, nome_arquivo: str):
        texto_importado = self.importar_arquivo(nome_arquivo)
        self.roteiro_organizado = self.processar_texto(texto_importado)

    def get_cena(self, id_cena: int) -> Any:
        if not self.roteiro_organizado:
            print("não existe roteiro organizado")
            return None
        return self.roteiro_organizado[id_cena]

    def get_roteiro_organizado(self) -> list:
        if not self.roteiro_organizado:
            print("não existe roteiro organizado")
        return self.roteiro_organizado

    def printar_roteiro_organizado(self, indice_atual: int = 1, nivel: int = 0, visitados: set = None):
        if visitados is None:
            visitados = set()

        indentacao = "    " * nivel

        if indice_atual in visitados:
            print(f"{indentacao}{indice_atual} (subloop detectado -> próximo: {indice_atual})")
            return

        texto = " --> " + self.get_cena(indice_atual)[1]
        print(f"{indentacao}{indice_atual}{texto}")
        visitados.add(indice_atual)

        direcoes_disponiveis = [opcao[1] for opcao in self.get_cena(indice_atual)[2]]

        for proximo_indice in direcoes_disponiveis:
            if proximo_indice in visitados:
                print(f"{indentacao}    {proximo_indice} (subloop)")
            else:
                self.printar_roteiro_organizado(proximo_indice, nivel + 1, visitados.copy())
