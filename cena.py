#imports
from palco import Palco
from texto import Texto
from opcoes import Opcoes

class Cena:
    def __init__(self,  cena_formato_lista):
        self.cena_id = cena_formato_lista[3]

        nome = cena_formato_lista[0]
        texto = cena_formato_lista[1]
        opcoes = cena_formato_lista[2]
        imagem_id = cena_formato_lista[3]
        
        self.palco = Palco(30,70,480,320, imagem_id)
        self.texto = Texto(70,440,400,120, texto, nome)
        self.opcoes = Opcoes(540,200,230,192, opcoes)

        # print("iniciou classe Cena, cena atual: ", self.cena_id)
        pass


    def draw(self,jogo):# implementar classe que controla a janela principal e a imagem princiapal, PALCO
    
        if self.palco:
            self.palco.draw(jogo) 
        if self.texto:
            self.texto.draw(jogo)
        if self.opcoes:
            self.opcoes.draw(jogo)
        # print(self.get_palco())

    def update(self):
        if self.palco:
            self.palco.update()
        if self.texto:
            self.texto.update()
        if self.opcoes:
            self.opcoes.update()
        pass


    def get_cena_id(self):
        return self.cena_id
    def get_palco(self):#mudando
        return self.palco
    def get_texto(self):
        return self.texto
    def get_opcoes(self):
        return self.opcoes
    def get_nome_opcao(self, indice):
        return self.opcoes.get_nome_opcao(indice)
# ----------------------------------------------------------------------------------------------------------


class GerenciadorCena:
    def __init__(self, jogo):

        self.jogo = jogo
        self.roteiro = self.jogo.roteiro
        self.cena_atual = None
        self.possivel_interagir = False
        self.frame_count = 0  # Contador de frames
        self.ativacao_iniciada = False  # Flag para iniciar a sequência de ativação
        # self.
        pass

    def get_opcoes_qtd(self):
        return self.cena_atual.get_opcoes().get_opcoes_qtd() if self.cena_atual else 0

    def carregar_cena(self, id_cena):
        if self.jogo.historico.get_ultima_cena() != id_cena:
            self.jogo.historico.adicionar(id_cena)
        self.cena_atual = Cena(self.roteiro.get_cena(id_cena) + [id_cena])
        
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
        opcoes = self.cena_atual.get_opcoes().get_opcoes()
        direcao_a_ir = opcoes[opcao_selecionada][1]
        # print("CONFIRMA ! direção:", direcao_a_ir)
        self.carregar_cena(direcao_a_ir)
        self.ativar_cena_atual()
    def rotina_de_abertura(self):
        sequencia_ativacoes = [0, 10, 80]  # Momentos para ativação dos elementos
        
        if self.frame_count == sequencia_ativacoes[0]:
            self.cena_atual.get_palco().ativar(0) #0 = instantaneo
            
        # Ativa o texto após 150 frames
        if self.frame_count == sequencia_ativacoes[1]:
            self.cena_atual.get_texto().ativar()
            
        # Ativa as opções após 250 frames
        if self.frame_count == sequencia_ativacoes[2]:
            self.cena_atual.get_opcoes().ativar()
            
            self.possivel_interagir = True  # Permite interações após ativação completa
            self.ativacao_iniciada = False  # Finaliza a sequência de ativação

        self.frame_count += 1  # Incrementa o contador de frames
        pass

    def update(self):
        # Controle de ativação sequencial baseado em frames
        if self.ativacao_iniciada:
            self.rotina_de_abertura() #sequencia de ativação do palco, texto e opções, em ordem.

        # Processa as ações do jogador
        if self.possivel_interagir:
            acao_feita = self.jogo.controle.verifica_teclas()
            if acao_feita == 'confirma':
                self.confirmar_opcao()
            elif acao_feita == 'acima':
                self.cena_atual.get_opcoes().selecionar_atras()
            elif acao_feita == 'abaixo':
                self.cena_atual.get_opcoes().selecionar_afrente()
            elif acao_feita == 'salvar':
                self.jogo.historico.salvar()
            elif acao_feita == 'carregar':
                self.jogo.historico.carregar()
                self.carregar_cena(self.jogo.historico.get_ultima_cena())
                self.ativar_cena_atual()

        if self.cena_atual:
            self.cena_atual.update()
