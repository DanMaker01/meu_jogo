
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
    def definir_mod(self, nome, valor_):
        self.mods[nome] = valor_
        pass
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
    
    def interpretar_item(self, item): #      +,-,*,/,=
        nome, simb, val = item
        if simb in ['+', '-']:
            self.alterar_mod(nome, val)
        elif simb in ['*', '/']:
            # self.remover_mod(nome)
            print("#implementar")
        elif simb == '=':
            self.definir_mod(nome, val)
        else:
            print("erro ao interpretar item:", item)
            pass