# Jogo da Velha em Python

Este é um simples jogo da velha (também conhecido como "tic-tac-toe") implementado em Python, onde dois jogadores se alternam para marcar posições em um tabuleiro 3x3, até que um jogador consiga alinhar três de seus símbolos (X ou O) em uma linha, coluna ou diagonal.

## Descrição

O jogo da velha é jogado em um tabuleiro 3x3. Dois jogadores, um jogando com "X" e o outro com "O", escolhem posições numeradas de 1 a 9 para marcar seu símbolo no tabuleiro. O jogo continua até que um jogador vença, criando uma linha de três símbolos consecutivos, ou até que todas as posições sejam ocupadas, resultando em um empate.

## Funcionalidades

- **Inicialização do Tabuleiro:** O tabuleiro é representado por uma lista de 9 elementos, iniciada com espaços vazios.
- **Exibição do Tabuleiro:** O tabuleiro é exibido no console, mostrando as posições escolhidas pelos jogadores.
- **Verificação de Vencedor:** O jogo verifica após cada jogada se algum jogador conseguiu formar uma linha, coluna ou diagonal com três símbolos iguais.
- **Verificação de Empate:** O jogo detecta automaticamente quando todas as posições do tabuleiro estão ocupadas, resultando em um empate.
- **Controle de Turnos:** O jogo alterna entre os jogadores "X" e "O" após cada jogada.

## Como jogar

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado.
3. Execute o jogo:

```bash
python jogo_da_velha.py
