from janelas import Janela


class Pressao:
    def __init__(self) -> None:
        #
        self.janela = Janela(0, 0, 200, 200, texto="")
        self.barra = Janela(0, 0, 200, 200, texto="", cor=(255, 255, 0))
        self.tempo = 0
        self.tempo_total = 0
        self.ativo = False
        pass

    def avancar_tempo(self):
        self.tempo -= 1
        pass

    def checar_se_tempo_acabou(self):
        if self.tempo <= 0:
            return True
        else:
            return False

    def desenhar(self):
        self.janela.desenhar()
        self.barra.desenhar()
        pass

    def ativar(self):
        self.ativo = True
        self.janela.ativar()
        self.barra.ativar()
        pass

    def desativar(self):
        self.ativo = False
        self.janela.desativar()
        self.barra.desativar()
        pass
    
    def update(self):
        if self.ativo:
            self.avancar_tempo()
        else:
            pass

