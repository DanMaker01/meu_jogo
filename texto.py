import janelas
class Texto:
    def __init__(self, jogo):
        print("iniciou classe Texto")
        self.jogo = jogo
        self.x = 90
        self.y= 410
        self.largura = 360
        self.altura = 120
        self.cor = (0, 0, 0)
        self.janela = janelas.Janela(jogo, self.x, self.y, self.largura, self.altura, ativa=True, texto="", cor=self.cor)
        self.texto = ""
        # self.janela = 

    def draw(self):
        self.janela.draw()
        pass


