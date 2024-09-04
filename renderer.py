# implementar Animação (ao invés de renderer.py)

import pygame

class Renderer:
    def __init__(self,jogo):
        self.jogo = jogo
        self.controle = jogo.controle

        self.cor_neutra = (0, 0, 0)
        
        self.font = jogo.font
        self.font_color = (20,20,20)
        self.margem_x = 10
        self.margem_y = 10
        self.espacamento_linhas = 20
        pass
    
    def desenhar_bg(self):
        imagem = self.jogo.recursos.get_img(0) # a imagem 0 é o BG
        self.jogo.screen.blit(imagem, (0,0))
        pass

    
    def desenhar_imagem(self, indice_imagem, x, y):
        # print("desenhar imagem", indice_imagem, x, y)
        imagem = self.jogo.recursos.get_img(indice_imagem)
        
        if imagem:
            self.jogo.screen.blit(imagem, (x, y), (0,0,imagem.get_width(),imagem.get_height()))
        else:
            print("imagem "+str(indice_imagem)+" não existe")
        pass    

    def desenhar_texto(self, texto, x, y, largura_max=0, altura_max=0):
        # Se largura_max ou altura_max forem 0, define um valor muito grande para não limitar
        if largura_max == 0:
            largura_max = float('inf')
        if altura_max == 0:
            altura_max = float('inf')

        altura_linha = self.font.get_height()

        while texto:
            largura_linha = 0
            linha_atual = ""
            palavras = texto.split(' ')
            
            for palavra in palavras:
                largura_palavra, _ = self.font.size(palavra)
                
                # Verifica se a palavra cabe na linha atual
                if largura_linha + largura_palavra + (self.font.size(' ')[0] if linha_atual else 0) > largura_max:
                    # Se a linha estiver vazia e a palavra é muito larga, pode ser necessário quebrar a palavra
                    if not linha_atual:
                        # Quebra a palavra em partes que cabem na largura
                        while largura_palavra > largura_max:
                            linha_atual = palavra[:1]
                            while self.font.size(linha_atual)[0] <= largura_max and len(linha_atual) < len(palavra):
                                linha_atual += palavra[len(linha_atual)]
                            if len(linha_atual) < len(palavra):
                                texto = palavra[len(linha_atual):]
                            else:
                                texto = ""
                            largura_linha = self.font.size(linha_atual)[0]
                            label = self.font.render(linha_atual, 1, self.font_color)
                            self.jogo.screen.blit(label, (x, y))
                            y += altura_linha
                            linha_atual = ""
                        continue

                    # Renderiza a linha atual e move para a próxima linha
                    label = self.font.render(linha_atual, 1, self.font_color)
                    self.jogo.screen.blit(label, (x, y))
                    y += altura_linha
                    largura_linha = 0
                    linha_atual = ""
                
                # Adiciona a palavra à linha atual
                if linha_atual:
                    linha_atual += " "
                linha_atual += palavra
                largura_linha += largura_palavra + self.font.size(' ')[0]

            # Renderiza a última linha, caso exista
            if linha_atual:
                label = self.font.render(linha_atual, 1, self.font_color)
                self.jogo.screen.blit(label, (x, y))
                y += altura_linha

            # Atualiza o texto restante, que será processado na próxima iteração do loop
            texto = texto[len(linha_atual) + 1:].lstrip()

            # Verifica se ainda há espaço para desenhar mais linhas
            if y + altura_linha > altura_max:
                # print("não tem espaço para desenhar mais linhas")
                break



    def desenhar_hud(self):
        texto_1 = "FPS: "+str(self.jogo.clock.get_fps())
        label = self.font.render(texto_1, 1, self.font_color)
        self.jogo.screen.blit(label, (self.margem_x, self.margem_y))
        # Texto dinâmico
        texto_2 = "cena: "+str(self.jogo.gerenciador_cena.get_cena_atual_id())
        label = self.font.render(texto_2, 1, self.font_color)
        self.jogo.screen.blit(label, (self.margem_x, self.margem_y + self.espacamento_linhas))
        # texto3
        texto_3 = "qtd_opcoes "+str(self.jogo.gerenciador_cena.get_opcoes_qtd())
        label = self.font.render(texto_3, 1, self.font_color)
        self.jogo.screen.blit(label, (self.margem_x, self.margem_y + self.espacamento_linhas*2))
        
        #texto4
        

        
        pass
