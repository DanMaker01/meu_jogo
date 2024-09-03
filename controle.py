

class Controle:
    def __init__(self):
        self.teclas_apertadas = []
        print("iniciou classe Controle")
        pass
    
    def add_teclas_apertadas(self, tecla):
        self.teclas_apertadas.append(tecla)
        pass

    def get_teclas_apertadas(self):
        return self.teclas_apertadas
    
    def limpar_teclas_apertadas(self):
        self.teclas_apertadas = []
        pass
    
    def get_ultima_tecla_apertada(self): #pode ser um combo de teclas
        return self.teclas_apertadas[-1]
    
    def update(self):
        lista_teclas = []
        for tecla in self.teclas_apertadas:
            lista_teclas.append(tecla)
        
        if lista_teclas: # se houver algo na lista (de teclas apertados)
            print("apertou:",lista_teclas)
            result = self.verifica_teclas()
            if result == 'confirma':
                print("confirma")
            elif result == 'acima':
                print("acima")
            elif result == 'abaixo':
                print("abaixo")


            self.limpar_teclas_apertadas()

    def verifica_teclas(self):
        teclas_confirma = ['space', 'enter']
        teclas_acima = ['up', 'w']
        teclas_abaixo = ['down', 's']
        
        if self.teclas_apertadas in teclas_confirma:
            return 'confirma'
        elif self.teclas_apertadas in teclas_acima:
            return 'acima'
        elif self.teclas_apertadas in teclas_abaixo:
            return 'abaixo'
        else:
            return 'nenhum'
