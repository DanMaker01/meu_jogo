
# modificadores
# tipos de modificadores:
#   - booleanos
#   - inteiros
#   - float?
#   - percentual?




class GerenciadorMods:
    def __init__(self):
        self.dicionario_mod = {}

        print("iniciou classe GerenciadorMods")

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
    def remover_mod(self, nome):
        self.dicionario_mod.pop(nome)
        pass
    def get_mod(self, nome):
        return self.dicionario_mod[nome]
    def print_mods(self):
        print(self.dicionario_mod)
        pass
