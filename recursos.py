import pygame
#adicionar testes de erro caso não impote imagens e sons direitos
#implementar audio

class Recursos:
    def __init__(self):
        #carregar todas imagens
        self.imgs = []
        lista_imgs_a_importar = ["bg.png","1.png"]
        self.carregar_todas_imagens(lista_imgs_a_importar)
        

        ##audio #implementar depois
        # pygame.mixer.init()
        # self.audios = []
        # lista_imgs_a_importar = ["audio1.mp3","audio2.mp3"]
        # self.carregar_todos_audios(lista_audios_a_importar)
        #...
        pass

    def carregar_todas_imagens(self, lista_a_importar):
        for img in lista_a_importar:
            self.imgs.append(self.scale_image(self.load_image(img),1.0))
            print(len(self.imgs),"imagens carregados.")
        pass
    @staticmethod
    def load_image(nome,path="recursos/"):
        return pygame.image.load(path+nome)

    @staticmethod
    def load_sound(nome,path="recursos/"):
        return pygame.mixer.Sound(path+nome)

    @staticmethod
    def scale_image(image, scale):
        width, height = image.get_size()
        new_size = (int(width * scale), int(height * scale))
        return pygame.transform.scale(image, new_size)

    def get_bg_img(self):
        return self.bg

    def get_img(self, indice):
        if indice>=0 and indice<len(self.imgs):
            return self.imgs[indice]