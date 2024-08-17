# Função para inicializar o tabuleiro
def inicializar_tabuleiro():
    return [' ' for _ in range(9)]

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print('---------')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print('---------')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    # Todas as combinações possíveis de vitória
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for combinacao in combinacoes_vencedoras:
        if all(tabuleiro[pos] == jogador for pos in combinacao):
            return True
    return False

# Função para verificar se o tabuleiro está cheio
def tabuleiro_cheio(tabuleiro):
    return ' ' not in tabuleiro

# Função para jogar o jogo da velha
def jogar():
    tabuleiro = inicializar_tabuleiro()
    jogador_atual = 'X'
    
    while True:
        exibir_tabuleiro(tabuleiro)
        try:
            posicao = int(input(f'Jogador {jogador_atual}, escolha uma posição (1-9): ')) - 1
            if tabuleiro[posicao] != ' ':
                print("Posição já ocupada, escolha outra.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Escolha uma posição de 1 a 9.")
            continue

        tabuleiro[posicao] = jogador_atual

        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f'Jogador {jogador_atual} venceu!')
            break
        elif tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print('Empate!')
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
