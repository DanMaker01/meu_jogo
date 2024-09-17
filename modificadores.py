
# modificadores
# tipos de modificadores:
#   - booleanos
#   - inteiros
#


# definição Modificador


class GerenciadorMods:
    def __init__(self):
        self.dicionario_mod = {}

        pass
    
    def alterar_mod(self, nome, valor_):
        #verifica se há o nome na lista self.modificadores, se existe, incrementa o valor
        if nome in self.dicionario_mod:
            self.dicionario_mod[nome] = self.dicionario_mod[nome] + valor_
        else:
            self.dicionario_mod[nome] = valor_
        return
    def zerar_mod(self, nome):
        self.dicionario_mod[nome] = 0
        pass
    def get_mod(self, nome):
        return self.dicionario_mod[nome]
    def print_mod(self):
        print(self.dicionario_mod)
    

