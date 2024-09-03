from typing import Any


class Roteiro:
    def __init__(self):
        print("Iniciou classe Roteiro")
        self.local = ""
        self.roteiro_organizado = []
        self.gerar_roteiro('roteiro1.txt')
        pass

    def get_endereco_completo(self, nome_arquivo):
        return self.local + nome_arquivo

    def importar_arquivo(self, nome_arquivo):
        endereco_completo = self.get_endereco_completo(nome_arquivo)
        with open(endereco_completo, 'r', encoding='utf-8') as file:
            texto_importado_bruto = file.read()
        return texto_importado_bruto
    
    def processar_texto(self, texto_importado_bruto):
        if not texto_importado_bruto:
            print("não importou direito")
            pass
        
        linhas = texto_importado_bruto.strip().split('\n')
        resultado = []

        for linha in linhas:
            partes = linha.split('@')
            nome = partes[0]
            texto = partes[1]
            opcoes_brutas = partes[2:]
            
            opcoes = []
            for opcao in opcoes_brutas:
                chave, valor = opcao.split(':')
                opcoes.append([chave, int(valor)])

            resultado.append([nome, texto, opcoes])

        return resultado
    
    def gerar_roteiro(self, nome_arquivo):
        self.roteiro_organizado = self.processar_texto(self.importar_arquivo(nome_arquivo))
        for linha in self.roteiro_organizado:
            print("linha",self.roteiro_organizado.index(linha),":",linha)
        pass

    def get_cena(self, id_cena):
        if self.roteiro_organizado:
            return self.roteiro_organizado[id_cena]
        else:
            print("não existe roteiro organizado")

    def get_roteiro_organizado(self):
        if self.roteiro_organizado:
            return self.roteiro_organizado
        else:
            print("não existe roteiro organizado")