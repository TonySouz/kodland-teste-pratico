# type: ignore

import random
from pygame import Rect
import pgzrun

# --- Configurações ---
WIDTH, HEIGHT = 800, 480
GRAVITY = 0.8
game_state = "menu"
sound_on = True

# --- Botões ---
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = Rect(x, y, w, h)
        self.text = text
        self.color = (0, 150, 255)

    def draw(self):
        screen.draw.filled_rect(self.rect, self.color)
        screen.draw.textbox(self.text, self.rect, color="black")

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

button_start = Button(300, 160, 200, 50, "Start")
button_sound = Button(300, 230, 200, 50, f"Sound: On")
button_exit = Button(300, 300, 200, 50, "Exit")
button_back = Button(300, 340, 200, 40, "Menu")

# --- Personagens ---
class Character:
    def __init__(self, x, y, w, h, color):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.vx, self.vy = 0, 0
        self.color = color
        self.on_ground = True
        self.dir = 1

    def rect(self):
        return Rect(int(self.x - self.w / 2), int(self.y - self.h), self.w, self.h)

    def draw(self):
        screen.draw.filled_rect(self.rect(), self.color)

class Hero(Character):
    def __init__(self, x, y):
        super().__init__(x, y, 34, 54, (40, 180, 40))

    def update(self):
        self.vx = 0
        if keyboard.left:
            self.vx = -3
            self.dir = -1
        if keyboard.right:
            self.vx = 3
            self.dir = 1
        if keyboard.space and self.on_ground:
            self.vy = -12
            self.on_ground = False

        self.vy += GRAVITY
        self.y += self.vy
        self.x += self.vx

        # Limites do chão
        if self.y >= HEIGHT - 50:
            self.y = HEIGHT - 50
            self.vy = 0
            self.on_ground = True
        self.x = max(20, min(WIDTH - 20, self.x))

class Enemy(Character):
    def __init__(self, x, y, a, b):
        super().__init__(x, y, 32, 48, (200, 30, 30))
        self.a, self.b = a, b
        self.vx = random.choice([-2, 2])

    def update(self):
        self.x += self.vx
        if self.x < self.a or self.x > self.b:
            self.vx *= -1

# --- Inicialização ---
def reset_game():
    global player, enemies
    player = Hero(150, HEIGHT - 50)
    enemies = [Enemy(450, HEIGHT - 50, 400, 600),
               Enemy(650, HEIGHT - 50, 620, 760)]

reset_game()

# --- Desenho ---
def draw_menu():
    screen.clear()
    screen.draw.text("PLATFORMER", (280, 80), fontsize=50)
    for b in [button_start, button_sound, button_exit]:
        b.draw()

def draw_game():
    screen.clear()
    # chão
    screen.draw.filled_rect(Rect(0, HEIGHT - 50, WIDTH, 50), (80, 50, 20))
    player.draw()
    for e in enemies:
        e.draw()

def draw_gameover():
    screen.clear()
    screen.draw.text("GAME OVER", (300, 200), fontsize=60)
    button_back.draw()

def draw():
    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        draw_game()
    elif game_state == "gameover":
        draw_gameover()

# --- Atualização ---
def update():
    global game_state
    if game_state == "playing":
        player.update()
        for e in enemies:
            e.update()
        if any(player.rect().colliderect(e.rect()) for e in enemies):
            game_state = "gameover"

# --- Entrada do mouse ---
def on_mouse_down(pos):
    global game_state, sound_on
    if game_state == "menu":
        if button_start.clicked(pos):
            reset_game()
            game_state = "playing"
        elif button_sound.clicked(pos):
            sound_on = not sound_on
            button_sound.text = f"Sound: {'On' if sound_on else 'Off'}"
        elif button_exit.clicked(pos):
            quit()
    elif game_state == "gameover" and button_back.clicked(pos):
        game_state = "menu"

pgzrun.go()
