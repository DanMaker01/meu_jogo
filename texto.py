import janelas
class Texto:
    def __init__(self,x,y,lar,alt, texto):

        print("iniciou classe Texto")
        self.x = x
        self.y= y
        self.largura = lar
        self.altura = alt
        self.cor = (0, 0, 0)
        self.janela = janelas.Janela(self.x, self.y, self.largura, self.altura, texto="", cor=self.cor)
        self.texto = ""
        # self.janela = 

    def draw(self,jogo):
        self.janela.draw(jogo)
        pass

    def ativar(self):
        self.janela.ativar()
        pass
