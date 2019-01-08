from os import system


def verifica_jogada(jogada):
    if len(jogada) != 2:
        return 1
    elif ('A' in jogada[0] or 'B' in jogada[0] or 'C' in jogada[0]) and \
            ('1' in jogada[1] or '2' in jogada[1] or '3' in jogada[1]):
        return 0
    else:
        return 1


def converte_jogada(jogada):
    if jogada[0] == 'A':
        jogada[0] = 1
    elif jogada[0] == 'B':
        jogada[0] = 2
    elif jogada[0] == 'C':
        jogada[0] = 3
    jogada[0] = int(jogada[0])
    jogada[1] = int(jogada[1])
    return jogada


def verifica_espaco_livre(tabuleiro, jogada):
    if tabuleiro[jogada[0]][jogada[1]] != " ":
        return 0
    else:
        return 1


def verifica_vencedor(tabuleiro):
    if (tabuleiro[1][1] == tabuleiro[1][2] == tabuleiro[1][3]) and tabuleiro[1][1] != ' ':
        return tabuleiro[1][1]
    elif (tabuleiro[2][1] == tabuleiro[2][2] == tabuleiro[2][3]) and tabuleiro[2][1] != ' ':
        return [2][1]
    elif (tabuleiro[3][1] == tabuleiro[3][2] == tabuleiro[3][3]) and tabuleiro[3][1] != ' ':
        return [3][1]
    elif (tabuleiro[1][1] == tabuleiro[2][1] == tabuleiro[3][1]) and tabuleiro[1][1] != ' ':
        return tabuleiro[1][1]
    elif (tabuleiro[1][2] == tabuleiro[2][2] == tabuleiro[3][2]) and tabuleiro[1][2] != ' ':
        return [1][2]
    elif (tabuleiro[1][3] == tabuleiro[2][3] == tabuleiro[3][3]) and tabuleiro[1][3] != ' ':
        return [1][3]
    elif (tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3]) and tabuleiro[1][1] != ' ':
        return tabuleiro[1][1]
    elif (tabuleiro[3][1] == tabuleiro[2][2] == tabuleiro[1][3]) and tabuleiro[3][1] != ' ':
        return tabuleiro[3][1]
    else:
        return ' '


def desenha_tabuleiro(linha, tabuleiro, jogada, contador, mensagem, vencedor=0):
    system("clear")
    if contador != 0:
        if tabuleiro[jogada[0]][jogada[1]] != " ":
            mensagem = "Já está ocupado otário."
        elif contador % 2 == 1:
            tabuleiro[jogada[0]][jogada[1]] = 'X'
            mensagem = "É a vez da O otário."
        else:
            tabuleiro[jogada[0]][jogada[1]] = 'O'
            mensagem = "É a vez do X otário."

    print(linha)
    print("J O G O  D A  V E L H A".center(36))
    print("\n")
    for i in range(0, 4):
        for j in range(0, 4):
            if j == 0:
                print(f"      {tabuleiro[i][j]}  ", end='')
            elif i == 0:
                print(f"   {tabuleiro[i][j]}  ", end='')
            else:
                print(f"  [{tabuleiro[i][j]}] ", end='')
        print('\n')
    print(f" {linha} ")
    print("|             AVISOS               |")
    print("|----------------------------------|")
    if vencedor == ('X' or 'O'):
        mensagem = f"O vencedor foi {vencedor} otário"
        print(f"|{mensagem.center(34)}|")
    elif contador == 9 or (jogada[0] == 9 and jogada[1] == 9):
        print("|   Ninguém venceu seus otários.   |")
    else:
        print(f"|{mensagem.center(34)}|")
    print(f" {linha} ")


# COMEÇA O PROGRAMA;
linha = ("_" * 34)
jogada = [0, 0]
contador = 0
mensagem = "Digite a linha e a coluna otário"
tabuleiro = [[' ', '1', '2', '3'],
             ['A', ' ', ' ', ' '],
             ['B', ' ', ' ', ' '],
             ['C', ' ', ' ', ' ']]

while True:
    while True:
        desenha_tabuleiro(linha, tabuleiro, jogada, contador, mensagem)
        if verifica_vencedor(tabuleiro) != ' ' or contador == 9:
            break
        else:
            jogada = list((input("> ")).upper())
            if jogada[0] and jogada[1] == '9':
                break
            elif verifica_jogada(jogada) == 0:
                converte_jogada(jogada)
                if tabuleiro[jogada[0]][jogada[1]] == ' ':
                    contador += 1
                    break
            else:
                mensagem = "Digita certo otário."

    if ((jogada[0] and jogada[1]) == '9') or (verifica_vencedor(tabuleiro) != ' ') or (contador == 9):
        converte_jogada(jogada)
        desenha_tabuleiro(linha, tabuleiro, converte_jogada(jogada), contador, mensagem, verifica_vencedor(tabuleiro))
        break
