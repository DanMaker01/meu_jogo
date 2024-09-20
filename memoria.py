import os

class Memoria:

    def __init__(self, jogo, nome_arquivo):
        print("iniciou classe Memoria")
        self.nome_arquivo = nome_arquivo
        self.jogo = jogo

        pass

    def salvar(self):
        print("salvando")
        historico_save = self.jogo.historico.gerar_save()
        mods_save = self.jogo.modificadores.gerar_save()
        print("h:",historico_save)
        print("m:",mods_save)

        try:
            if not os.path.exists(self.nome_arquivo):
                print(f"Arquivo {self.nome_arquivo} nao encontrado, criando um novo.")
            with open(self.nome_arquivo, 'w') as arquivo:
                
                for id_cena in historico_save:
                    arquivo.write(str(id_cena) + '\n')
                
                arquivo.write('\n')
                        
                for nome, valor in mods_save:
                    arquivo.write(f"{nome}:{valor}\n")
                pass
        except IOError as e:
            print("Erro ao salvar o historico:", e)

    def carregar(self):
        print("carregando arquivo:", self.nome_arquivo)
        try:
            if not os.path.exists(self.nome_arquivo):
                print(f"Arquivo {self.nome_arquivo} não encontrado.")
                return

            with open(self.nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
            
            # Separar o histórico dos modificadores
            historico_lido = []
            mods_lidos = {}

            # Processar o histórico até encontrar a linha em branco
            leitura_mods = False
            for linha in linhas:
                linha = linha.strip()  # Remove espaços e quebras de linha extras
                
                if linha == '':
                    leitura_mods = True  # A partir da linha em branco, começamos a ler modificadores
                    continue
                
                if not leitura_mods:
                    # Leitura do histórico (antes da linha em branco)
                    try:
                        id_cena = int(linha)
                        historico_lido.append(id_cena)
                    except ValueError as e:
                        print(f"Erro ao ler o histórico: {e}")
                else:
                    # Leitura dos modificadores (depois da linha em branco)
                    try:
                        nome, valor = linha.split(":")
                        # Tentar converter o valor para o tipo correto (int, float, etc.)
                        if '.' in valor:
                            valor = float(valor)
                        else:
                            valor = int(valor)
                        mods_lidos[nome] = valor
                    except ValueError as e:
                        print(f"Erro ao ler modificadores: {e}")

            # Atualizar o jogo com os dados carregados
            self.jogo.historico.carregar_save(historico_lido)
            for nome, valor in mods_lidos.items():
                self.jogo.modificadores.definir_mod(nome, valor)

            # print("Histórico carregado:", historico_lido)
            # print("Modificadores carregados:", mods_lidos)

        except IOError as e:
            print(f"Erro ao carregar o jogo: {e}")
