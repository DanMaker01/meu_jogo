import janelas
import jogo
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
        margem_x = 5
        margem_y = 5
        jogo.renderer.desenhar_texto(self.texto, self.x + margem_x, self.y + margem_y, 360-margem_x, 120-margem_y)
        pass
    def update(self):
        if self.janela:
            self.janela.update()
    def ativar(self):
        self.janela.ativar()
        pass

    def desativar(self):
        self.janela.desativar()
        pass

    def iluminar(self, tempo_milisegundos= 200):
        self.janela.iluminar(tempo_milisegundos)
        pass