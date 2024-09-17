from typing import Any

class Roteiro:
    def __init__(self):
        print("Iniciou classe Roteiro")
        # self.jogo = jogo
        self.local = ""
        self.roteiro_organizado = []
        self.gerar_roteiro('roteiro1.txt')
        print(self.printar_roteiro_organizado())
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
                chave, valor = opcao.split('#')
                opcoes.append([chave, int(valor)])

            resultado.append([nome, texto, opcoes])

        return resultado
    
    def gerar_roteiro(self, nome_arquivo):
        self.roteiro_organizado = self.processar_texto(self.importar_arquivo(nome_arquivo))
        # for linha in self.roteiro_organizado:
        #     print("linha",self.roteiro_organizado.index(linha),":",linha)
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

    #implementar outro tipo de visualização
    def printar_roteiro_organizado(self, indice_atual=1, nivel=0, visitados=None):
        if visitados is None:
            visitados = set()

        # Imprime o índice atual com a indentação correspondente ao nível
        indentacao = "    " * nivel

        # Verifica se o índice já foi visitado para identificar subloops
        if indice_atual in visitados:
            print(f"{indentacao}{indice_atual} (subloop detectado -> próximo: {indice_atual})")
            return

        #printar o indice e o texto daquele nó
        texto = " --> "+self.get_cena(indice_atual)[1]
        
        print(f"{indentacao}{indice_atual}{texto}") #aquiiiiii <------ aquiiii <-------

        # Marca o índice atual como visitado
        visitados.add(indice_atual)

        # Obtenha as direções disponíveis no nó atual
        linha_atual = self.roteiro_organizado[indice_atual]
        direcoes_disponiveis = [opcao[1] for opcao in linha_atual[2]]

        # Percorre recursivamente os filhos, se ainda não foram visitados
        for proximo_indice in direcoes_disponiveis:
            if proximo_indice in visitados:
                print(f"{indentacao}    {proximo_indice} (subloop)")
            else:
                self.printar_roteiro_organizado(proximo_indice, nivel + 1, visitados.copy())
    
    