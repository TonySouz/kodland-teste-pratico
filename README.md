# Survival Game

## Descrição

`Survival Game` é um jogo de plataforma 2D desenvolvido usando `Python` e a biblioteca `Pygame Zero`. O jogador controla um herói que deve sobreviver atacando zumbis que surgem continuamente. O jogo possui animações para correr, pular e atirar, além de efeitos sonoros e música de fundo.

---

## Como Jogar

* **Movimentação:** Use as setas do teclado (`←` e `→`) para mover o herói.
* **Pular:** Pressione `↑` para pular.
* **Atirar:** Pressione `Espaço` para atirar.
* **Menu:** No menu principal, clique nos botões:

  * **Start:** Inicia o jogo.
  * **Music ON/OFF:** Liga ou desliga a música de fundo.
  * **Quit:** Sai do jogo.

---

## Controles

| Ação                  | Tecla / Botão |
| --------------------- | ------------- |
| Mover para a esquerda | ←             |
| Mover para a direita  | →             |
| Pular                 | ↑             |
| Atirar                | Espaço        |
| Iniciar o jogo        | Start button  |
| Ligar/Desligar música | Music button  |
| Sair do jogo          | Quit button   |

---

## Requisitos

* Python 3.x
* Pygame Zero

### Instalação do Pygame Zero

```bash
pip install pgzero
```

---

## Estrutura do Projeto

```
SurvivalGame/
│
├── main.py             # Script principal do jogo
├── images/             # Pasta com todas as imagens do herói, tiros e zumbis
│   ├── base/           # Animações de idle do herói
│   ├── run/            # Animações de corrida do herói
│   ├── jump/           # Animações de pulo do herói
│   ├── fire/           # Animações de tiro do herói
│   ├── zombie/         # Animações dos zumbis
│   └── dead/           # Animações de morte dos zumbis
├── sounds/             # Pasta com sons e efeitos do jogo
│   ├── fire.wav
│   └── jump.wav
└── README.md           # Este arquivo
```

---

## Estrutura do Código

* **Configurações da Janela:** Define largura, altura e título.
* **Estados do Jogo:** `menu`, `playing`, `gameover`.
* **Herói:** Configurações, animações (idle, corrida, pulo, tiro), movimentação e colisões.
* **Zumbis:** Geração, animações e colisões.
* **Balas:** Criação, movimentação e detecção de colisão com zumbis.
* **Menu:** Botões Start, Music e Quit.
* **Som e Música:** Funções para tocar efeitos sonoros e música de fundo.
* **Funções de Update e Draw:** Atualiza a lógica e renderiza gráficos na tela.

---

## Animações

* **Herói Idle:** `base/base1`, `base/base2`, `base/base3`
* **Corrida:** `run/run1` a `run/run4` (direita), `run/run1-1` a `run/run4-4` (esquerda)
* **Pulo:** `jump/jump1` a `jump/jump3`
* **Tiro:** `fire/fire1` a `fire/fire3`
* **Zumbis:** `zombie/zombie1` a `zombie/zombie4`
* **Morte de Zumbis:** `dead/dead1` a `dead/dead3`

---

## Sons

* `fire.wav`: Som de tiro.
* `jump.wav`: Som de pulo.
* Música de fundo: `theme.mp3` (reproduzida no menu e durante o jogo).

---

## Como Rodar

No terminal, execute:

```bash
pgzrun main.py
```

Certifique-se de que todas as pastas (`images` e `sounds`) estejam no mesmo diretório que o script principal `main.py`.

---

## Observações

* O jogo é simples e serve como base para expandir com mais funcionalidades, inimigos e power-ups.
* Para adicionar mais animações, basta criar as imagens e atualizar as listas correspondentes no código.

---

## Licença

Este projeto é gratuito para uso educacional e pessoal. Você pode modificar e distribuir o código, desde que mantenha os créditos originais