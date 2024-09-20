#imports
import os

#classe Historico
class Historico:
    def __init__(self):
        self.historico = []
        print("iniciou classe Historico")
        pass

    def get_ultima_cena(self):
        if len(self.historico) == 0:
            return None
        return self.historico[-1]
    
    def adicionar(self, id_cena):
        self.historico.append(id_cena)
        # print("historico:",self.historico)
        pass

    # def is_vazio(self):
    #     if len(self.historico) == 0:
    #         return True
    #     return False
    def gerar_save(self):
        """
        Salva o historico em um arquivo.
        
        Verifica se o historico nao esta vazio antes de salvar.
        """
        if self.historico:
            # print("salvando historico: ", self.historico)
            save = self.historico
            return save 
        else:
            print("Nao ha historico para salvar.")

    def carregar_save(self, historico_save):
        # print("carregando historico_save:",historico_save)
        self.historico = historico_save


        pass