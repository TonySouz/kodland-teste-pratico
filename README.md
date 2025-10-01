# 🧟 SURVIVAL

**Plataforma:** Python (Pygame Zero)
**Gênero:** Ação / Sobrevivência

## 🎮 Descrição

**SURVIVAL** é um jogo de ação 2D onde o jogador controla um herói que deve sobreviver a hordas de zumbis. Movimente-se para esquerda ou direita, atire nos inimigos e tente sobreviver o maior tempo possível.

O jogo possui:

* Menu interativo com botões para iniciar, ativar/desativar música e sair do jogo.
* Animações de corrida e tiro do herói.
* Zumbis que surgem continuamente e perseguem o jogador.
* Sons para tiros e acertos, além de música de fundo opcional.

## ⌨️ Controles

* **Setas esquerda/direita:** Movimentar o herói.
* **Espaço:** Atirar.
* **Mouse:** Selecionar opções do menu.

## 🛠 Requisitos

* Python 3.7 ou superior
* [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/)
* Assets organizados na estrutura de pastas usada no código:

  ```
  base/          # imagens do herói parado
  run/           # imagens da corrida do herói
  fire/          # imagens do tiro
  zombie/        # imagens dos zumbis
  dead/          # imagens dos zumbis mortos
  sounds/        # arquivos de som (hit, fire, etc.)
  music/         # música tema
  ```

## ▶️ Como Jogar

1. Abra o terminal e navegue até a pasta do jogo.
2. Execute o comando:

   ```bash
   pgzrun game.py
   ```
3. Use os controles para jogar e sobreviver aos ataques dos zumbis.
4. Divirta-se!

## ⚠️ Observações

* A música pode ser ligada ou desligada no menu.
* Cada tiro elimina o zumbi mais próximo do herói.
* O jogo termina quando um zumbi toca o herói.

## 📝 Créditos

Feito por **Tony Souza**