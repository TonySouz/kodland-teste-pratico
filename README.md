# Platformer Pygame Zero

Um jogo de plataforma simples feito com **Pygame Zero**.
Controle um herói que precisa evitar inimigos patrulheiros 
enquanto se movimenta pelo cenário.

---

## 🎮 Controles

* **Seta esquerda / Seta direita**: mover o herói
* **Espaço**: pular
* **Mouse**: clicar nos botões do menu e Game Over

---

## 🖥️ Requisitos

* Python 3.x
* [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/)

Instalação do Pygame Zero via pip:

```bash
pip install pgzero
```

---

## 🚀 Como rodar

1. Salve o arquivo do jogo, por exemplo: `game.py`
2. Abra o terminal na pasta do arquivo
3. Execute:

```bash
pgzrun game.py
```

O jogo abrirá em uma janela e estará pronto para jogar.

---

## 📝 Funcionalidades

* Menu principal com botões:

  * **Start**: iniciar o jogo
  * **Sound On/Off**: alternar sons (placeholder para futuras melhorias)
  * **Exit**: fechar o jogo
* Game Over com botão para voltar ao menu
* Herói com movimento lateral e pulo
* Inimigos que patrulham entre limites definidos
* Detecção de colisão entre herói e inimigos

---

## 🔧 Estrutura do Código

* **Character**: classe base para heróis e inimigos
* **Hero**: personagem controlável
* **Enemy**: inimigos patrulheiros
* **Button**: classe para gerenciar botões do menu
* **Funções**:

  * `draw_menu()`, `draw_game()`, `draw_gameover()` → desenham as telas
  * `update()` → lógica de movimentação e colisão
  * `on_mouse_down(pos)` → interação com botões
  * `reset_game()` → reinicia herói e inimigos

---

## 🌟 Melhorias Futuras

* Adicionar plataformas flutuantes
* Sons para pulo, colisão e pontuação
* Sistema de pontuação
* Animações para o herói e inimigos

---

## 📄 Licença

Este projeto é open-source e pode ser usado e modificado livremente.