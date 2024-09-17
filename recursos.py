import pygame
#adicionar testes de erro caso não impote imagens e sons direitos

class Recursos:
    def __init__(self):
        print("iniciou classe Recursos")
        #carregar todas imagens
        self.imgs = []
        lista_imgs_a_importar = ["bg.png"] # a imagem 0 é o BG, 

        #carregar todas cenas numeradas
        #jeito A
        qtd_cenas = 13
        for i in range(1,qtd_cenas+1):
            lista_imgs_a_importar.append(str(i)+".png")
        print("importar:",lista_imgs_a_importar, "TAM:",len(lista_imgs_a_importar))

        #carregar tudo que estiver na lista_imgs_a_importar de uma vez só
        self.carregar_todas_imagens(lista_imgs_a_importar,)
        
        ##audio #implementar depois
        # pygame.mixer.init()
        # self.audios = []
        # lista_imgs_a_importar = ["audio1.mp3","audio2.mp3"]
        # self.carregar_todos_audios(lista_audios_a_importar)
        #...
        pass

    def carregar_todas_imagens(self, lista_a_importar):
        for string_img in lista_a_importar:
            self.imgs.append([string_img,self.scale_image(self.load_image(string_img),1.0)])
            if self.imgs[-1][1] is None:
                print("erro ao carregar imagem:",string_img)
            else:
                pass
                # print("carregou imagem:",string_img)
        # print(len(self.imgs),"imagens carregadas.")
        pass
    @staticmethod
    def load_image(nome,path="recursos/"):
        return pygame.image.load(path+nome).convert_alpha()

    @staticmethod
    def load_sound(nome,path="recursos/"):
        return pygame.mixer.Sound(path+nome)

    @staticmethod
    def scale_image(image, scale):
        width, height = image.get_size()
        new_size = (int(width * scale), int(height * scale))
        return pygame.transform.scale(image, new_size)


    def get_img(self, indice):
        if indice>=0 and indice<len(self.imgs):
            # print(self.imgs[indice])
            return self.imgs[indice][1]