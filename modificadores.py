
# modificadores
# tipos de modificadores:
#   - booleanos
#   - inteiros
#   - float?
#   - percentual?




class GerenciadorMods:
    def __init__(self):
        self.inventario = {}

        print("iniciou classe GerenciadorMods")

        pass
    
    def alterar_mod(self, nome, valor_):
        #verifica se há o nome na lista self.modificadores, se existe, incrementa o valor
        if nome in self.inventario:
            self.inventario[nome] = self.inventario[nome] + valor_
        else:
            self.inventario[nome] = valor_
        return
    def zerar_mod(self, nome):
        self.inventario[nome] = 0
        pass
    def remover_mod(self, nome):
        self.inventario.pop(nome)
        pass
    def get_mod(self, nome):
        return self.inventario[nome]
    def print_mods(self):
        print(self.inventario)
        pass
    def get_inventario(self):
        return self.inventario