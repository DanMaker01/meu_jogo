#imports


#classe Historico
class Historico:
    def __init__(self):
        self.nome_arquivo = "historico.txt"
        self.historico = []

        pass

    def get_ultima_cena(self):
        if len(self.historico) == 0:
            return 0
        return self.historico[-1]
    

    def adicionar(self, id_cena):
        self.historico.append(id_cena)
        print("historico:",self.historico)
        pass
    def salvar(self):
        print("salvando historico: ", self.historico)
        #salvar self.historico em um arquivo
        with open(self.nome_arquivo, 'w') as arquivo:
            for id_cena in self.historico:
                arquivo.write(str(id_cena) + '\n')
        pass

    def carregar(self):
        #carregar o historico de um arquivo
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    self.historico.append(int(linha.strip()))
            print("historico:",self.historico)
        except FileNotFoundError:
            pass
