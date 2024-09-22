#imports
import random
from palco import Palco
from texto import Texto
from opcoes import Opcoes
from pressao import Pressao

class Cena:
    def __init__(self,  jogo, cena_formato_lista):
        self.cena_id = cena_formato_lista[3]
        self.jogo = jogo

        nome = cena_formato_lista[0]
        texto = cena_formato_lista[1]
        opcoes = cena_formato_lista[2]
        imagem_id = cena_formato_lista[3]
        
        self.palco = Palco(30,70,480,320, imagem_id)
        self.texto = Texto(70,440,400,120, texto, nome, jogo)
        self.opcoes = Opcoes(540,200,230,192, opcoes, jogo)
        self.pressao = Pressao(540,400,230,16)

        # print("iniciou classe Cena, cena atual: ", self.cena_id)
        pass
    def draw(self,jogo):
    
        if self.palco:
            self.palco.draw(jogo) 
        if self.texto:
            self.texto.draw(jogo)
        if self.opcoes:
            self.opcoes.draw(jogo)
        if self.pressao:
            self.pressao.draw(jogo)
        # print(self.get_palco())

    def update(self):
        if self.palco:
            self.palco.update()
        if self.texto:
            self.texto.update()
        if self.opcoes:
            self.opcoes.update()
        if self.pressao:
            self.pressao.update()
        
        pass
    def get_cena_id(self):
        return self.cena_id
    def get_palco(self):
        return self.palco
    def get_texto(self):
        return self.texto
    def get_opcoes(self):
        return self.opcoes
    def get_pressao(self):
        return self.pressao
    def get_nome_opcao(self, indice):
        return self.opcoes.get_nome_opcao(indice)
# ----------------------------------------------------------------------------------------------------------


class GerenciadorCena:
    def __init__(self, jogo):

        self.jogo = jogo
        self.cena_atual = None
        self.possivel_interagir = False
        self.frame_count = 0            # Contador de frames
        self.ativacao_iniciada = False  # Flag para iniciar a sequência de ativação
        # self.
        pass
    def get_opcoes_qtd(self):
        return self.cena_atual.get_opcoes().get_opcoes_qtd() if self.cena_atual else 0

    def carregar_cena(self, id_cena):
        if self.jogo.historico.get_ultima_cena() != id_cena:
            self.jogo.historico.adicionar(id_cena)
        self.cena_atual = Cena(self.jogo, self.jogo.roteiro.get_cena(id_cena) + [id_cena])
        
    def get_cena_atual_id(self):
        return self.cena_atual.get_cena_id() if self.cena_atual else None

    def ativar_cena_atual(self):
        """
        Inicia a ativação da cena atual, controlada por um contador de frames.
        """
        self.frame_count = 0  # Reinicia o contador de frames
        self.ativacao_iniciada = True  # Inicia a sequência de ativação
        self.possivel_interagir = False  # Bloqueia interações durante a ativação
        pass

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
        lista_opcoes = self.cena_atual.get_opcoes().get_opcoes()
        
        #verifica se ganha item ao escolher esta opção
        item_operacao_valor = lista_opcoes[opcao_selecionada][3]
        if item_operacao_valor != None: # se tem item como premio
            self.jogo.modificadores.interpretar_item(item_operacao_valor)

        direcao_a_ir = lista_opcoes[opcao_selecionada][1]
        # print("CONFIRMA ! direção:", direcao_a_ir)
        self.carregar_cena(direcao_a_ir)    #carrega a proxima cena
        # self.ativar_cena_atual()            # Ativa a proxima cena
    def rotina_de_abertura(self):
        sequencia_ativacoes = [0, 10, 70, 80]  # Momentos para ativação dos elementos
        #ativa o texto apos 0 frames
        if self.frame_count == sequencia_ativacoes[0]:
            self.cena_atual.get_palco().ativar(0) #0 = instantaneo (sem fade)
            
        # Ativa o texto após 10 frames
        if self.frame_count == sequencia_ativacoes[1]:
            self.cena_atual.get_texto().ativar()
            
        # Ativa as opções após 70 frames
        if self.frame_count == sequencia_ativacoes[2]:
            #ativar tudo
            self.cena_atual.get_opcoes().ativar()
            
        # Ativa as opções após 80 frames
        if self.frame_count == sequencia_ativacoes[3]:
            self.cena_atual.get_pressao().ativar()
            
            tempo_de_texto = self.cena_atual.get_texto().get_qtd_letras_texto() * fator_tempo_cada_letra
            tempo_de_opcoes = 0
            fator_tempo_cada_letra = 7
            for opcao in self.cena_atual.get_opcoes().get_opcoes():
                tempo_de_opcoes += len(opcao[0]) * fator_tempo_cada_letra

            self.cena_atual.get_pressao().ativar_tempo(tempo_de_texto+tempo_de_opcoes)
            self.possivel_interagir = True  # Permite interações após ativação completa
            self.ativacao_iniciada = False  # Finaliza a sequência de ativação
            
        self.frame_count += 1  # Incrementa o contador de frames
        pass

    def update(self):
        # Controle de ativação sequencial baseado em frames
        if self.ativacao_iniciada:
            self.rotina_de_abertura() #sequencia de ativação do palco, texto e opções, em ordem.

        # # Processa as ações do jogador
        # if self.possivel_interagir:
        #     self.verifica_acoes_jogador()

        if self.cena_atual:
            
            if self.cena_atual.get_pressao().checar_se_tempo_acabou():

                id_opcao_aleatoria = random.randrange(0, self.get_cena_atual().get_opcoes().get_qtd_opcoes_reais())

                print("opcao selecionada:",id_opcao_aleatoria)
                self.cena_atual.get_opcoes().set_opcao_selecionada(id_opcao_aleatoria)
                self.confirmar_opcao()
                self.ativar_cena_atual()

            self.cena_atual.update()
        pass
    
    def is_possivel_interagir(self):
        return self.possivel_interagir
