import janelas
class Texto:
    def __init__(self,x,y,lar,alt, texto):

        print("iniciou classe Texto")
        self.x = x
        self.y= y
        self.largura = lar
        self.altura = alt
        self.cor = (150, 150, 150)
        self.janela = janelas.Janela(self.x, self.y, self.largura, self.altura, texto="", cor=self.cor)
        self.texto = texto
        # self.janela = 

    def draw(self,jogo):
        self.janela.draw(jogo)
        margem_x = 10
        margem_y = 10
        jogo.renderer.desenhar_texto(self.texto, self.x + margem_x, self.y + margem_y)
        pass

    def ativar(self):
        self.janela.ativar()
        pass
