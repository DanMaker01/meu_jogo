from janelas import Janela

class Opcoes: #está meio bugado #Implementar
    def __init__(self, x, y, lar, alt, opcoes):
        # print("iniciou classe Opções")
        pos_x = x
        pos_y = y
        largura = lar
        altura = alt
        _cor = (200, 200, 200)
        self.janela = Janela(pos_x, pos_y, largura, altura, cor=_cor)
        self.ativar_interacao = False
        self.opcoes = opcoes
        self.opcoes_janelas = []
        self.distancia_entre_opcoes = alt / len(self.opcoes)
        self.opcao_selecionada = 0
        self.cor_opcao_selecionada = (255, 200, 30)

        # Cria as janelas das opções
        margem_x = 2
        margem_y = 2
        for i in range(len(self.opcoes)):
            _x = pos_x + margem_x
            _y = pos_y + self.distancia_entre_opcoes * i + 0.5 * margem_y
            _largura = largura - 2 * margem_x
            _altura = alt / len(self.opcoes) - margem_y
            _texto = self.opcoes[i][0]
            _cor = (255, 255, 255)
            janela_i = Janela(_x, _y, _largura, _altura, texto=_texto, cor=_cor)
            self.opcoes_janelas.append(janela_i)

        self.alpha = 0  # Transparência inicial para o fade-in
        self.max_alpha = 255  # Transparência máxima
        self.fading_in = False  # Controle para o efeito de fade-in
        self.fade_speed = 0  # Velocidade do fade-in

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
            
            if self.opcoes:
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

    def get_opcoes_qtd(self):
        return len(self.opcoes)

    def set_opcao_escolhida(self, indice):
        self.opcao_escolhida = indice

    def get_opcao_selecionada(self):
        return self.opcao_selecionada

    def selecionar_afrente(self):
        self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)

    def selecionar_atras(self):
        self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)

    def selecionar_opcao(self, indice):
        self.opcao_selecionada = indice
