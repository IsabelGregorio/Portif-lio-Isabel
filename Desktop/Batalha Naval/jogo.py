

import random

class Navio:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.posicoes = []
        self.partes_atingidas = 0 
        
        

    @property
    def afundou(self) -> bool:
        return self.partes_atingidas >= self.tamanho
    
class Tabuleiro:
    def __init__ (self, tamanho=5):
        self.tamanho = tamanho
        self.grelha = [["~" for _ in range(tamanho)] for _ in range(tamanho)]
        self.navios = []   

    def exibir(self, revelar_navios:bool = False):
        print(" "+" ".join(str(i) for i in range(self.tamanho)))

        for index_linha, linha in enumerate(self.grelha):
            linha_visual = []
            for caractere in linha:
                if caractere == "N" and not revelar_navios:
                    linha_visual.append("~") 
                else:
                    linha_visual.append(caractere)
            print(f"{index_linha} " + " ".join(linha_visual))  
    
    def posicionar_navio_aleatorio(self, navio: Navio):
        posicionado = False
        while not posicionado:
            linha = random.randint(0, self.tamanho - 1)
            coluna_inicial = random.randint(0, self.tamanho - navio.tamanho)
            espaco_livre = all(self.grelha[linha][coluna_inicial + i] == "~" for i in range(navio.tamanho))

            if espaco_livre:
                for i in range(navio.tamanho):
                    c = coluna_inicial + i
                    self.grelha[linha][c] = "N"
                    navio.posicoes.append((linha, c))
                self.navios.append(navio)
                posicionado = True

    def dar_tiro(self, linha: int, coluna: int) -> str:
        if self.grelha[linha][coluna] == "N":
            self.grelha[linha][coluna] = "X"

            for navio in self.navios:
                if (linha, coluna) in navio.posicoes:
                    navio.partes_atingidas += 1
                    if navio.aundou:
                        return f"FOGO! Você afundou o {navio.nome}!"
                    return "ÁGUA! Nenhum navio ali."
                
                return "Você ja atirou nessa coordenada antes!"