class JogoDaVelha:

  def __init__(self):
    self.tabuleiro = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    self.jogador_atual = 'O'

  def imprimir_tabuleiro(self):
    for linha in self.tabuleiro:
      print(' | '.join(linha))

  def jogar(self):
    while True:
      print('')
      self.imprimir_tabuleiro()

      linha = int(
        input(f'Jogador {self.jogador_atual}, escolha a linha (0-2): '))
      coluna = int(
        input(f'Jogador {self.jogador_atual}, escolha a coluna (0-2): '))

      if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print('Posição inválida. Tente novamente.')
        continue
      elif self.tabuleiro[linha][coluna] != '-':
        print('Essa posição já está ocupada. Tente novamente.')
        continue

      self.tabuleiro[linha][coluna] = self.jogador_atual

      # Verifica se o jogador atual venceu
      if self.verificar_vencedor():
        print('')
        self.imprimir_tabuleiro()
        print(f'O jogador {self.jogador_atual} venceu!')
        return

      # Verifica se houve empate
      if self.verificar_empate():
        print('')
        self.imprimir_tabuleiro()
        print('O jogo terminou em empate!')
        return

      # Muda o jogador atual
      self.jogador_atual = 'X' if self.jogador_atual == 'O' else 'O'

  def verificar_vencedor(self):
    for i in range(3):
      # Verifica se há três em linha na horizontal
      if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][
          2] != '-':
        return True
            
      # Verifica se há três em linha na vertical
      elif self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][
          i] != '-':
        return True
            
    # Verifica se há três em linha na diagonal
    if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][
        2] != '-':
      return True
    elif self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][
        0] != '-':
      return True
    else:
      return False

  def verificar_empate(self):
    for linha in self.tabuleiro:
      if '-' in linha:
        return False
    return True


jogo = JogoDaVelha()
jogo.jogar()
