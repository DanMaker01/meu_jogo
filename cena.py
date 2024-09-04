#imports
from roteiro import Roteiro
from janelas import Janela
from texto import Texto
from opcoes import Opcoes

class Cena:
    def __init__(self,  cena_formato_lista):
        texto = cena_formato_lista[1]
        opcoes = cena_formato_lista[2]
        imagem_id = cena_formato_lista[3]


        self.janela_principal = Janela(30,70,480,320) #implementar melhor
        self.texto = Texto(90,410,360,120, texto)
        self.opcoes = Opcoes(540,200,230,192, opcoes)
        self.imagem_id = imagem_id
        pass

    def get_cena_id(self):
        return self.imagem_id
    def get_janela_principal(self):
        return self.janela_principal
    def get_texto(self):
        return self.texto
    def get_opcoes(self):
        return self.opcoes
    def get_nome_opcao(self, indice):
        return self.opcoes.get_nome_opcao(indice)

    def draw(self,jogo):
        if self.janela_principal:
            self.janela_principal.draw(jogo)
            jogo.renderer.desenhar_imagem(self.imagem_id, self.janela_principal.x, self.janela_principal.y)
        if self.texto:
            self.texto.draw(jogo)
        if self.opcoes:
            self.opcoes.draw(jogo)

# -----------------------------------------------------------------

class GerenciadorCena:
    def __init__(self, jogo):
        self.roteiro = Roteiro()
        self.jogo = jogo
        
        self.cena_atual = None

        self.possivel_interagir = False
        pass
    
    def get_opcoes_qtd(self):
        if self.cena_atual:
            return self.cena_atual.get_opcoes().get_opcoes_qtd()
        
    def carregar_cena(self, id_cena):
        #implementar
        print("carregando cena:", id_cena)
        cena_formato_lista = self.roteiro.get_cena(id_cena) #elementos [nome, texto, opcoes ]
        cena_formato_lista.append(id_cena)                  #elementos [nome, texto, opcoes, id_img]
        self.cena_atual = Cena(cena_formato_lista)
        pass

    def get_cena_atual_id(self):
        if self.cena_atual:
            return self.cena_atual.get_cena_id()
    def ativar_cena_atual(self):
        if self.cena_atual:
            print("Ativou a cena!")
            self.cena_atual.get_janela_principal().ativar()
            self.cena_atual.get_texto().ativar()
            self.cena_atual.get_opcoes().ativar()
            self.ativar_interacao()
        pass
    def desativar_cena(self):
        if self.cena_atual:
            self.cena_atual.get_janela_principal().desativar()
            self.cena_atual.get_texto().desativar()
            self.cena_atual.get_opcoes().desativar()
            self.possivel_interagir = False
            pass
        else:
            print("Nenhuma cena está ativa para ser desativada")
    def desativar_interacao(self):
        self.possivel_interagir = False
        pass
    def ativar_interacao(self):
        self.possivel_interagir = True
        pass
    def get_cena_atual(self):
        return self.cena_atual
    
    def draw(self,jogo):
        if self.cena_atual:
            self.cena_atual.draw(jogo)
        else:
            print("não há cena ativa")

    def get_opcao_selecionada(self):
        if self.cena_atual:
            return self.cena_atual.get_opcoes().get_opcao_selecionada()

    def confirmar_opcao(self):
        print("CONFIRMA !")
        opcao_selecionada = self.cena_atual.get_opcoes().get_opcao_selecionada()
        opcoes = self.cena_atual.get_opcoes().get_opcoes()
        direcao_a_ir = opcoes[opcao_selecionada][1]
        self.carregar_cena(direcao_a_ir)
        # print("opcao escolhida:", opcao_selecionada)
        # print("texto:", opcoes[opcao_selecionada][0])
        # print("direcao:", opcoes[opcao_selecionada][1])
                
    def update(self):
        if self.possivel_interagir:
            acao_feita = self.jogo.controle.verifica_teclas()
            if acao_feita == 'confirma':
                self.confirmar_opcao()
            elif acao_feita == 'acima':
                self.cena_atual.get_opcoes().selecionar_atras()
            elif acao_feita == 'abaixo':
                self.cena_atual.get_opcoes().selecionar_afrente()
            else:
                #não apertou nada, só continua o loop...
                pass
            
        pass