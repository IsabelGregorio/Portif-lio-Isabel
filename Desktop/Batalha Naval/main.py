from jogo import Tabuleiro, Navio

def jogar():
    print("=== BEM-VINDO À BATALHA NAVAL ===")
    tabuleiro_computador = Tabuleiro()

    submarino = Navio("Submarino", 2)
    tabuleiro_computador.posicionar_navio_aleatorio(submarino)

    tentativas = 10

    while tentativas > 0:
        print(f"\nTentativas restantes: {tentativas}")
        tabuleiro_computador.exibir(revelar_navios=False)
        try:
                linha = int(input("Escolha a linha (0-4):"))
                coluna = int(input("Escolha a coluna (0-4):"))

                if not (0 <= linha < 5 and 0 <= coluna < 5):
                        print("Coordenadas fora do tabuleiro! Tente novamente.")
                continue
            
                resultado = tabuleiro_computador.dar_tiro(linha, coluna)
                print(f"\n-> {resultado}")

                if all(navio.afundou for navio in tabuleiro_computador.navios):
                        print("\nPARABENS! Você destruiu a frota inimiga!")
                tabuleiro_computador.exibir(revelar_navios=True)
                
                break

                tentativas -= 1
            
        except ValueError:
            
                print("Por favor, digite números válidos.")
    
    else:
        print("\nFim de Jogo! Suas tentativas acabaram.")
        print("Onde estava os navios:")
        tabuleiro_computador.exibir(revelar_navios=True)

if  __name__ == "__main__":
        jogar()




