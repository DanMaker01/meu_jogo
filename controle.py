

class Controle:
    def __init__(self):
        self.teclas_apertadas = []
        print("iniciou controle.py")
        pass
    
    def add_teclas_apertadas(self, tecla):
        self.teclas_apertadas.append(tecla)
        pass

    def limpar_teclas_apertadas(self):
        self.teclas_apertadas = []
        pass

    def get_teclas_apertadas(self):
        return self.teclas_apertadas
    
    def get_teclas_apertadas_ultima(self):
        return self.teclas_apertadas[-1]