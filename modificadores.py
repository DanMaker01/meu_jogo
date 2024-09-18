
class GerenciadorMods:
    def __init__(self):
        self.mods = {}
        # print("iniciou classe GerenciadorMods")
        pass
    
    def alterar_mod(self, nome, valor_):
        #verifica se há o nome na lista self.modificadores, se existe, incrementa o valor
        if nome in self.mods:
            self.mods[nome] = self.mods[nome] + valor_
        else:
            self.mods[nome] = valor_
        return
    def zerar_mod(self, nome):
        self.mods[nome] = 0
        pass
    def remover_mod(self, nome):
        self.mods.pop(nome)
        pass
    def get_mod(self, nome):
        return self.mods[nome]
    
    def get_mods(self):
        return self.mods