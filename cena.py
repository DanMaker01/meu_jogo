#imports
from roteiro import Roteiro
from janelas import Janela

class Cena:
    def __init__(self,  cena_formato_lista):
        nome = cena_formato_lista[0]
        texto = cena_formato_lista[1]
        opcoes = cena_formato_lista[2]
        imagem = cena_formato_lista[3]

        self.janela_principal = None #implementar
        self.texto = cena_formato_lista[1]
        self.opcoes = cena_formato_lista[2]
        pass

    def get_janela_principal(self):
        return self.janela_principal
    def get_texto(self):
        return self.texto
    def get_opcoes(self):
        return self.opcoes
    def draw(self,jogo):
        if self.janela_principal:
            self.janela_principal.draw(jogo)
        if self.texto:
            self.texto.draw(jogo)
        if self.opcoes:
            self.opcoes.draw(jogo)

        

class GerenciadorCena:
    def __init__(self, jogo):
        self.roteiro = Roteiro()
        self.jogo = jogo
        
        self.cena_atual = None

        self.possivel_interagir = False
        pass
    
    def carregar_cena(self, id_cena):
        #implementar
        cena_formato_lista = self.roteiro.get_cena(id_cena) #elementos [id_cena, nome, texto, opcoes ]
        cena_formato_lista.append(self.jogo.recursos.get_img(id_cena))
        print(cena_formato_lista[3].getwidth())
        # self.cena_atual = Cena(cena_formato_lista)
        pass

    def ativar_cena_atual(self):
        if self.cena_atual:
            self.ativar_janela_principal()
            self.ativar_texto()
            self.ativar_opcoes()
            self.possivel_interagir = True
        
        pass

    def get_cena_atual(self):
        return self.cena_atual
    def ativar_janela_principal(self):
        if self.cena_atual:
            print(self.cena_atual.get_janela_principal())
            self.cena_atual.get_janela_principal().ativar()
    def ativar_texto(self):
        if self.cena_atual:
            self.cena_atual.get_texto().ativar()
    def ativar_opcoes(self):
        if self.cena_atual:
            self.cena_atual.get_opcoes().ativar()
    def draw(self,jogo):
        if self.cena_atual:
            self.cena_atual.draw(jogo)
        else:
            print("não há cena ativa")

    def update(self):
        if self.possivel_interagir:
            
            pass
        pass