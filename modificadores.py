import os

class GerenciadorMods:
    def __init__(self, nome_arquivo="mods.txt"):
        self.mods = {}
        self.nome_arquivo = nome_arquivo

    def alterar_mod(self, nome, valor_):
        if nome in self.mods:
            self.mods[nome] += valor_
        else:
            self.mods[nome] = valor_

    def definir_mod(self, nome, valor_):
        self.mods[nome] = valor_

    def zerar_mod(self, nome):
        self.mods[nome] = 0

    def remover_mod(self, nome):
        self.mods.pop(nome, None)

    def get_mod(self, nome):
        return self.mods.get(nome, 0)

    def get_mods(self):
        return self.mods

    def interpretar_item(self, item):
        nome, simb, val = item
        if simb in ['+', '-']:
            self.alterar_mod(nome, val)
        elif simb in ['*', '/']:
            print("#implementar")
        elif simb == '=':
            self.definir_mod(nome, val)
        else:
            print("Erro ao interpretar item:", item)

    def gerar_save(self):
        """
        Salva os modificadores em um arquivo.
        
        Verifica se há modificadores antes de salvar.
        """
        if self.mods:
            save = []
            for nome, valor in self.mods.items():
                save.append([nome,valor])
            return save
            # print("Salvando modificadores:", self.mods)
            # try:
            #     if not os.path.exists(self.nome_arquivo):
            #         print(f"Arquivo {self.nome_arquivo} não encontrado, criando um novo.")
            #     with open(self.nome_arquivo, 'w') as arquivo:
            #         for nome, valor in self.mods.items():
            #             arquivo.write(f"{nome}:{valor}\n")
            # except IOError as e:
            #     print("Erro ao salvar os modificadores:", e)
        else:
            print("Não há modificadores para salvar.")

    def carregar(self):
        """
        Carrega os modificadores de um arquivo.
        
        O arquivo deve conter uma linha para cada modificador no formato 'nome:valor'.
        """
        print("Carregando modificadores")
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                self.mods = {}
                for linha in arquivo:
                    try:
                        nome, valor = linha.strip().split(':')
                        self.mods[nome] = int(valor)
                    except ValueError as e:
                        print(f"Erro ao carregar modificador na linha '{linha.strip()}':", e)
            print("Modificadores carregados:", self.mods)
        except FileNotFoundError:
            print(f"Arquivo {self.nome_arquivo} não encontrado.")
        except IOError as e:
            print("Erro ao carregar os modificadores:", e)
