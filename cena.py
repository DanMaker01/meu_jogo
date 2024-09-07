#imports
from roteiro import Roteiro
from janelas import Janela
from texto import Texto
from opcoes import Opcoes
from historico import Historico

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
            if self.janela_principal.luz == 1.0:
                jogo.renderer.desenhar_imagem(self.imagem_id, self.janela_principal.x, self.janela_principal.y)
            
        if self.texto:
            self.texto.draw(jogo)
        if self.opcoes:
            self.opcoes.draw(jogo)

    def update(self):
        if self.janela_principal:
            self.janela_principal.update()
        if self.texto:
            self.texto.update()
        if self.opcoes:
            self.opcoes.update()
        pass

# -----------------------------------------------------------------

class GerenciadorCena:
    def __init__(self, jogo):
        self.roteiro = Roteiro(jogo)
        self.historico = Historico()
        self.jogo = jogo
        self.cena_atual = None
        self.possivel_interagir = False


        self.flag_ativar_janela_principal = 0
        self.flag_desativar_janela_principal = 0
        self.flag_ativar_texto = 0
        self.flag_desativar_texto = 0
        self.flag_ativar_opcoes = 0
        self.flag_desativar_opcoes = 0


    def get_opcoes_qtd(self):
        return self.cena_atual.get_opcoes().get_opcoes_qtd() if self.cena_atual else 0

    def carregar_cena(self, id_cena):
        if self.historico.get_ultima_cena() != id_cena:
            self.historico.adicionar(id_cena)
        self.cena_atual = Cena(self.roteiro.get_cena(id_cena) + [id_cena])

    def get_cena_atual_id(self):
        return self.cena_atual.get_cena_id() if self.cena_atual else None

    def ativar_janela_principal(self, timer_milissegundos=200):
        self.flag_ativar_janela_principal = timer_milissegundos
        pass
    def desativar_janela_principal(self, timer_milissegundos=200):
        self.flag_desativar_janela_principal = timer_milissegundos
        pass

    def ativar_texto(self, timer_milissegundos=200):
        self.flag_ativar_texto = timer_milissegundos
        pass
    def desativar_texto(self, timer_milissegundos=200):
        self.flag_desativar_texto = timer_milissegundos
        pass

    def ativar_opcoes(self, timer_milissegundos=200):
        self.flag_ativar_opcoes = timer_milissegundos
        pass
    def desativar_opcoes(self, timer_milissegundos=200):
        self.flag_desativar_opcoes = timer_milissegundos
        pass
    def ativar_cena_atual(self):### implementar
        self.ativar_janela_principal(1)
        self.ativar_texto(1)
        self.ativar_opcoes(1)
        # self.cena_atual.get_janela_principal().ativar()
        # self.cena_atual.get_texto().ativar()
        # self.cena_atual.get_opcoes().ativar()
        self.possivel_interagir = True

    def desativar_cena(self):
        self.desativar_janela_principal()
        self.desativar_texto()
        self.desativar_opcoes()
        self.possivel_interagir = False

    def get_cena_atual(self):
        return self.cena_atual

    def draw(self, jogo):
        self.cena_atual.draw(jogo) if self.cena_atual else print("não há cena ativa")

    def get_opcao_selecionada(self):
        return self.cena_atual.get_opcoes().get_opcao_selecionada() if self.cena_atual else None

    def confirmar_opcao(self):
        opcao_selecionada = self.get_opcao_selecionada()
        opcoes = self.cena_atual.get_opcoes().get_opcoes()
        direcao_a_ir = opcoes[opcao_selecionada][1]
        print("CONFIRMA ! direção:", direcao_a_ir)
        self.carregar_cena(direcao_a_ir)

    def update(self):
        if self.possivel_interagir:
            acao_feita = self.jogo.controle.verifica_teclas()
            if acao_feita == 'confirma':
                self.confirmar_opcao()
            elif acao_feita == 'acima':
                self.cena_atual.get_opcoes().selecionar_atras()
            elif acao_feita == 'abaixo':
                self.cena_atual.get_opcoes().selecionar_afrente()
            elif acao_feita == 'salvar':
                self.historico.salvar()
            elif acao_feita == 'carregar':
                self.historico.carregar()
                self.carregar_cena(self.historico.get_ultima_cena())


        # ativar e desativar janelas, texto e opções com timer

        if self.flag_ativar_janela_principal > 0:
            self.flag_ativar_janela_principal -= 1
            if self.flag_ativar_janela_principal <= 0:
                print("ativou janela principal")
                self.cena_atual.get_janela_principal().ativar()
                self.cena_atual.get_janela_principal().iluminar(50)

        if self.flag_desativar_janela_principal > 0:
            self.flag_desativar_janela_principal -= 1
            if self.flag_desativar_janela_principal <= 0:
                self.cena_atual.get_janela_principal().desativar()

        if self.flag_ativar_texto > 0:
            
            self.flag_ativar_texto -= 1
            if self.flag_ativar_texto <= 0:
                print("ativou texto")
                self.cena_atual.get_texto().ativar()
                self.cena_atual.get_texto().iluminar(60)

        if self.flag_desativar_texto > 0:
            self.flag_desativar_texto -= 1
            if self.flag_desativar_texto <= 0:
                self.cena_atual.get_texto().desativar()

        if self.flag_ativar_opcoes > 0:
            self.flag_ativar_opcoes -= 1
            if self.flag_ativar_opcoes <= 0:
                print("ativou opcoes")
                self.cena_atual.get_opcoes().ativar()
                self.cena_atual.get_opcoes().iluminar(70)

        if self.flag_desativar_opcoes > 0:
            self.flag_desativar_opcoes -= 1
            if self.flag_desativar_opcoes <= 0:
                self.cena_atual.get_opcoes().desativar()


        if self.cena_atual:
            self.cena_atual.update()
        

        pass

