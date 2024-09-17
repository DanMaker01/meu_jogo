#imports
import os

#classe Historico
class Historico:
    def __init__(self):
        self.nome_arquivo = "historico.txt"
        self.historico = []

        pass

    def get_ultima_cena(self):
        if len(self.historico) == 0:
            return None
        return self.historico[-1]
    
    def adicionar(self, id_cena):
        self.historico.append(id_cena)
        # print("historico:",self.historico)
        pass


    def salvar(self):
        """
        Salva o historico em um arquivo.
        
        Verifica se o historico nao esta vazio antes de salvar.
        """
        if self.historico:
            print("salvando historico: ", self.historico)
            try:
                if not os.path.exists(self.nome_arquivo):
                    print(f"Arquivo {self.nome_arquivo} nao encontrado, criando um novo.")
                with open(self.nome_arquivo, 'w') as arquivo:
                    for id_cena in self.historico:
                        arquivo.write(str(id_cena) + '\n')
            except IOError as e:
                print("Erro ao salvar o historico:", e)
        else:
            print("Nao ha historico para salvar.")

    def carregar(self):
        print("carregando historico")
        """
        Carrega o historico de um arquivo.
        
        O arquivo deve conter um numero por linha, representando cada cena
        visitada pelo jogador.
        """
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                
                self.historico = []
                for linha in arquivo:
                    try:
                        id_cena = int(linha.strip())
                        if id_cena is None:
                            raise ValueError("id_cena nao pode ser None")
                        self.historico.append(id_cena)
                    except ValueError as e:
                        print("Erro ao carregar o historico:", e)
            print("historico:",self.historico)
        except FileNotFoundError:
            print(f"Arquivo {self.nome_arquivo} nao encontrado.")
        except IOError as e:
            print("Erro ao carregar o historico:", e)
