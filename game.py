import pgzrun
from pygame import Rect

# --- CONFIGURAÇÕES DA JANELA ---
WIDTH = 800
HEIGHT = 600
TITLE = "Meu Jogo Base"

# --- CHÃO ---
ground_height = 50
ground_color = (169, 169, 169)
ground_offset = 0

# --- ESTADOS DO JOGO ---
game_state = "menu"  # "menu" | "playing" | "gameover"
music_on = True
sound_on = True

# --- HERÓI ---
hero_images_idle = ["base/base1", "base/base2", "base/base3"]
hero = Actor("base/base1", (WIDTH // 2, HEIGHT - ground_height))  # type: ignore
hero_idle_index = 0
hero_idle_timer = 0
hero_speed = 200
hero.bottom = HEIGHT - ground_height + ground_offset

# --- ANIMAÇÃO DE CORRIDA ---
hero_running_right = ["run/run1", "run/run2", "run/run3", "run/run4"]
hero_running_left = ["run/run1-1", "run/run2-2", "run/run3-3", "run/run4-4"]
hero_run_index = 0
hero_run_timer = 0
is_running = False
running_direction = "right"  # "right" ou "left"

# --- ANIMAÇÃO DE TIRO ---
hero_shooting = False
hero_shoot_timer = 0
hero_shoot_frame = 0
bullet_images = ["fire/fire1", "fire/fire2", "fire/fire3"]

# Lista de balas
bullets = []

# --- ANIMAÇÃO DE PULO ---
jump_images = ["jump/jump1", "jump/jump2", "jump/jump3"]
hero_jumping = False
jump_index = 0
jump_timer = 0
jump_velocity = 0
gravity = 900
jump_force = -500

# --- BOTÕES DO MENU ---
menu_buttons = {
    "start": Rect((WIDTH//2 - 100, 200), (200, 60)),
    "music": Rect((WIDTH//2 - 100, 300), (200, 60)),
    "quit": Rect((WIDTH//2 - 100, 400), (200, 60)),
}

# --- FUNÇÕES DE SOM/MÚSICA ---
def toggle_music():
    global music_on
    music_on = not music_on
    if music_on:
        music.play("theme")  # type: ignore
    else:
        music.stop()  # type: ignore

def toggle_sound():
    global sound_on
    sound_on = not sound_on

def play_sound(name):
    if sound_on:
        try:
            getattr(sounds, name).play() # type: ignore
        except AttributeError:
            print(f"Som '{name}' não encontrado!")

# --- ZUMBIS ---
zombies = []
zombie_images = ["zombie/zombie1", "zombie/zombie2", "zombie/zombie3", "zombie/zombie4"]
dead_images = ["dead/dead1", "dead/dead2", "dead/dead3"]
zombie_speed = 150
spawn_timer = 0
spawn_interval = 2.0

# --- UPDATE ---
def update(dt):
    global hero_idle_index, hero_idle_timer
    global hero_shooting, hero_shoot_timer, hero_shoot_frame
    global is_running, hero_run_index, hero_run_timer, running_direction
    global spawn_timer, zombies, game_state, bullets
    global hero_jumping, jump_velocity, jump_index, jump_timer

    if game_state != "playing":
        return

    is_running = False
    # Movimento do herói (esquerda/direita)
    if keyboard.left: # type: ignore
        hero.x -= hero_speed * dt
        if hero.x < hero.width // 2:
            hero.x = hero.width // 2
        is_running = True
        running_direction = "left"
    elif keyboard.right: # type: ignore
        hero.x += hero_speed * dt
        if hero.x > WIDTH - hero.width // 2:
            hero.x = WIDTH - hero.width // 2
        is_running = True
        running_direction = "right"

    # Pulo
    if hero_jumping:
        jump_velocity += gravity * dt
        hero.y += jump_velocity * dt
        jump_timer += dt
        if jump_timer > 0.15:
            jump_timer = 0
            jump_index = min(jump_index + 1, len(jump_images)-1)
            hero.image = jump_images[jump_index]

        # Se encostar no chão, para de pular
        if hero.bottom >= HEIGHT - ground_height + ground_offset:
            hero.bottom = HEIGHT - ground_height + ground_offset
            hero_jumping = False
            jump_index = 0
            jump_timer = 0
            hero_idle_index = 0
            hero.image = hero_images_idle[hero_idle_index]

    # Animações do herói
    if not hero_jumping:
        if is_running and not hero_shooting:
            hero_run_timer += dt
            if hero_run_timer > 0.1:
                hero_run_timer = 0
                hero_run_index = (hero_run_index + 1) % 4
                hero.image = hero_running_right[hero_run_index] if running_direction == "right" else hero_running_left[hero_run_index]
        elif not hero_shooting:
            hero_idle_timer += dt
            if hero_idle_timer > 0.3:
                hero_idle_timer = 0
                hero_idle_index = (hero_idle_index + 1) % len(hero_images_idle)
                hero.image = hero_images_idle[hero_idle_index]

    if hero_shooting:
        hero_shoot_timer += dt
        if hero_shoot_timer > 0.1:
            hero_shoot_timer = 0
            hero_shoot_frame += 1
            if hero_shoot_frame >= len(bullet_images):
                hero_shooting = False
                hero_shoot_frame = 0
                hero_idle_index = 0
                hero.image = hero_images_idle[hero_idle_index]
            else:
                hero.image = bullet_images[hero_shoot_frame]

    # Spawn de zumbis
    spawn_timer += dt
    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        zombie = Actor(zombie_images[0], (WIDTH + 50, HEIGHT - ground_height + ground_offset))  # type: ignore
        zombie.bottom = HEIGHT - ground_height + ground_offset
        zombie.frame_index = 0
        zombie.frame_timer = 0
        zombie.dying = False
        zombies.append(zombie)

    # Atualizar zumbis
    for zombie in zombies[:]:
        if hasattr(zombie, "dying") and zombie.dying:
            zombie.frame_timer += dt
            if zombie.frame_timer > 0.2:
                zombie.frame_timer = 0
                zombie.frame_index += 1
                if zombie.frame_index >= len(dead_images):
                    zombies.remove(zombie)
                else:
                    bottom_pos = zombie.bottom
                    zombie.image = dead_images[zombie.frame_index]
                    zombie.bottom = bottom_pos
            continue

        # zumbi vivo se move
        zombie.x -= zombie_speed * dt
        zombie.bottom = HEIGHT - ground_height + ground_offset

        zombie.frame_timer += dt
        if zombie.frame_timer > 0.2:
            zombie.frame_timer = 0
            zombie.frame_index = (zombie.frame_index + 1) % len(zombie_images)
            bottom_pos = zombie.bottom
            zombie.image = zombie_images[zombie.frame_index]
            zombie.bottom = bottom_pos

        # Colisão com herói
        if abs(zombie.x - hero.x) < 40:
            game_state = "gameover"

    # Atualizar balas
    for bullet in bullets[:]:
        bullet.y -= 500 * dt
        for zombie in zombies[:]:
            if bullet.colliderect(zombie) and not getattr(zombie, "dying", False):
                play_sound("hit")
                zombie.dying = True
                zombie.frame_index = 0
                zombie.frame_timer = 0
                zombie.image = dead_images[0]
                if bullet in bullets:
                    bullets.remove(bullet)
        if bullet.y < 0:
            bullets.remove(bullet)

# --- DRAW ---
def draw():
    screen.clear() # type: ignore
    if game_state == "menu":
        screen.draw.text("SURVIVAL", center=(WIDTH//2, 100), fontsize=50, color="white") # type: ignore
        screen.draw.filled_rect(menu_buttons["start"], "blue") # type: ignore
        screen.draw.text("Start", center=menu_buttons["start"].center, fontsize=40, color="white") # type: ignore
        screen.draw.filled_rect(menu_buttons["music"], "green") # type: ignore
        status = "ON" if music_on else "OFF"
        screen.draw.text(f"Music {status}", center=menu_buttons["music"].center, fontsize=40, color="white") # type: ignore
        screen.draw.filled_rect(menu_buttons["quit"], "red") # type: ignore
        screen.draw.text("Quit", center=menu_buttons["quit"].center, fontsize=40, color="white") # type: ignore
    elif game_state == "playing":
        ground_rect = Rect(0, HEIGHT - ground_height, WIDTH, ground_height)
        screen.draw.filled_rect(ground_rect, ground_color) # type: ignore
        hero.draw()
        for zombie in zombies:
            zombie.draw()
        for bullet in bullets:
            bullet.draw()
    elif game_state == "gameover":
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=80, color="red")  # type: ignore

# --- INPUT ---
def on_key_down(key):
    if game_state == "playing":
        if key == keys.SPACE:  # type: ignore
            shoot()
        elif key == keys.UP:  # type: ignore
            jump()

def on_mouse_down(pos):
    global game_state
    if game_state != "menu":
        return
    if menu_buttons["start"].collidepoint(pos):  # type: ignore
        game_state = "playing"
        if music_on:
            music.play("theme")  # type: ignore
    elif menu_buttons["music"].collidepoint(pos):  # type: ignore
        toggle_music()
    elif menu_buttons["quit"].collidepoint(pos):  # type: ignore
        exit()

# --- TIRO ---
def shoot():
    global hero_shooting, hero_shoot_timer, hero_shoot_frame
    hero_shooting = True
    hero_shoot_timer = 0
    hero_shoot_frame = 0
    hero.image = bullet_images[0]
    play_sound("fire")
    
    # Remover o zumbi mais próximo iniciando animação de morte
    alive_zombies = [z for z in zombies if not getattr(z, "dying", False)]
    if alive_zombies:
        alive_zombies.sort(key=lambda z: abs(z.x - hero.x))
        target = alive_zombies[0]
        target.dying = True
        target.frame_index = 0
        target.frame_timer = 0
        target.image = dead_images[0]

# --- PULO ---
def jump():
    global hero_jumping, jump_velocity, jump_index
    if not hero_jumping:
        hero_jumping = True
        jump_velocity = jump_force
        jump_index = 0
        hero.image = jump_images[jump_index]
        play_sound("jump")

# --- RODAR JOGO ---
pgzrun.go()  # type: ignore
