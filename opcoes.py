from janelas import Janela

#implementar
# o tamanho da janela deve ser de acordo com as opcoes sem requisito e opções com requisito cumprido
# ao mexer com a lista de opções, sempre usar a lista real, cuidado com escolher opcoes não liberadas
class Opcoes: #está meio bugado #Implementar
    def __init__(self, x, y, lar, alt, opcoes, jogo, _cor=(100, 100, 100)):
        # print("iniciou classe Opções")
        pos_x = x
        pos_y = y
        largura = lar
        altura = alt

        self.jogo = jogo
        # self.font_nome = font_nome #implementar, para que o menu se adapte ao tamanho do texto e qtd de opçoes
        self.janela = Janela(pos_x, pos_y, largura, altura, cor=_cor)
        self.ativar_interacao = False
        self.opcoes = opcoes
        self.opcoes_reais = []
        for opcao in self.opcoes:
            # print("opcao:",opcao)
            if opcao[2]:                             # se a opção tem condição
                if self.condicao_cumprida(opcao[2]): # verifica se a condição foi cumprida
                    self.opcoes_reais.append(opcao) # se a condição foi cumprida, esta opção vai ser representada realmente
                else:
                    pass   
            else: # a opção não tem requisição, logo é cumprida automaticamente
                self.opcoes_reais.append(opcao) 

        # print("opcoes:",self.opcoes)
        
        self.opcoes_janelas = []

        #
        self.distancia_entre_opcoes = alt / len(self.opcoes_reais)
        self.opcao_selecionada = 0
        self.cor_opcao_selecionada = (255, 220, 30)

        # Cria as janelas das opções
        margem_x = 2
        margem_y = 2
        for i in range(len(self.opcoes_reais)):
            _x = pos_x + margem_x
            _y = pos_y + self.distancia_entre_opcoes * i + 0.5 * margem_y
            _largura = largura - 2 * margem_x
            _altura = alt / len(self.opcoes_reais) - margem_y
            _texto = self.opcoes_reais[i][0]
            _cor = (255, 255, 255)
            janela_i = Janela(_x, _y, _largura, _altura, texto=_texto, cor=_cor)
            self.opcoes_janelas.append(janela_i)

        self.alpha = 0  # Transparência inicial para o fade-in
        self.max_alpha = 255  # Transparência máxima
        self.fading_in = False  # Controle para o efeito de fade-in
        self.fade_speed = 0  # Velocidade do fade-in
        pass
    def condicao_cumprida(self, condicao):
        # print("condicao:", condicao)
        nome_mod, condicional, valor = condicao

        # Verifica se o modificador existe
        valor_mod = self.jogo.modificadores.get_mods().get(nome_mod, None)
        
        if valor_mod is not None:  # Se o modificador existe
            if condicional == ">":
                return valor_mod > valor
            elif condicional == "<":
                return valor_mod < valor
            elif condicional == ">=":
                return valor_mod >= valor
            elif condicional == "<=":
                return valor_mod <= valor
            elif condicional == "==":
                return valor_mod == valor
            elif condicional == "!=":
                return valor_mod != valor
            else:
                return None  # Condicional inválida
        return None  # Modificador não encontrado

    def ativar(self, duracao_fade=50): #implementar #bug
        self.janela.ativar(duracao_fade)
        
        if duracao_fade > 0:

            if duracao_fade == 0:
                duracao_fade = 1
            for i in range(len(self.opcoes_janelas)):
                self.opcoes_janelas[i].ativar(duracao_fade + 1000 * i, max_alpha=128) #implementar, cada uma aparecer num tempo

            # Calcula a velocidade do fade-in baseada na duração
            self.fade_speed = self.max_alpha / duracao_fade
            
            self.fading_in = True  # Inicia o fade-in
            self.alpha = 0  # Inicia com transparência total (invisível)
        else:
            self.alpha = self.max_alpha
            self.fading_in = False

    def desativar(self):
        self.janela.desativar()


    def draw(self, jogo): #pensar se tá certo, para deixar independete cada janela de opcao #implementar
        if self.janela.ativa:
            self.janela.draw(jogo)
            
            if self.opcoes_reais:
                for janela in self.opcoes_janelas:
                    # Se o índice da janela está selecionado, desenha a opção em verde
                    if self.opcao_selecionada == self.opcoes_janelas.index(janela):
                        janela.set_cor(self.cor_opcao_selecionada)
                    else:
                        janela.set_cor_original()

                    # Se o texto da janela estiver vazio, coloca '>>'
                    if janela.get_texto() == "":
                        janela.set_texto(">>")
                    
                    # Atualiza a transparência da janela de opção
                    janela.set_alpha(self.alpha) #implementar, não há necessidade disso...

                    janela.draw(jogo)
            else:
                print("Nenhuma opção definida")

    def update(self):
        if self.janela:
            self.janela.update()
        
        for janela_opcao in self.opcoes_janelas:
            janela_opcao.update()

        # Controle de fade-in das janelas de opções
        if self.fading_in and self.alpha < self.max_alpha:
            self.alpha += self.fade_speed
            if self.alpha >= self.max_alpha:
                self.alpha = self.max_alpha  # Garante que não ultrapasse o valor máximo
                self.fading_in = False  # Finaliza o efeito de fade-in



    def adicionar_opcao(self, texto, direcao):
        self.opcoes.append([texto, direcao])
                
    def limpar_opcoes(self):
        self.opcoes = []
        
    def get_opcoes(self):
        return self.opcoes
    
    def set_opcao_selecionada(self, indice):
        self.opcao_selecionada = indice

    def get_opcao_selecionada(self):
        return self.opcao_selecionada

    def selecionar_afrente(self):
        self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes_reais)

    def selecionar_atras(self):
        self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes_reais)

    def selecionar_opcao(self, indice):
        self.opcao_selecionada = indice

    def get_qtd_opcoes_reais(self):
        return len(self.opcoes_reais)