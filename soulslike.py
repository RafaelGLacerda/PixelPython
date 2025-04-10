import random 
import pygame
import sys

pygame.init()
pygame.font.init()  # Inicializa o módulo de fontes

win = pygame.display.set_mode((800, 600))
player_idle = pygame.image.load("assets/guerreiro.png").convert_alpha()


# Fonte e cores
FONT = pygame.font.SysFont(None, 30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)



pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Soulslike")

# Teclas configuráveis (padrões)
key_bindings = {
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d,
    "dodge": pygame.K_SPACE,
    "attack": pygame.K_f
}
def main_menu():
    selected = 0
    options = ["Jogar", "Opções", "Sair"]
    title_font = pygame.font.SysFont(None, 64)

    while True:
        WIN.fill((30, 30, 30))
        pygame.draw.rect(WIN, (50, 50, 50), (200, 100, 400, 400), border_radius=15)

        title = title_font.render("Soulslike Game", True, (200, 200, 255))
        WIN.blit(title, (WIDTH//2 - title.get_width()//2, 130))

        for i, opt in enumerate(options):
            color = (100, 255, 100) if i == selected else (220, 220, 220)
            text = font.render(opt, True, color)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, 230 + i * 60))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected] == "Jogar":
                        return
                    elif options[selected] == "Opções":
                        key_config_menu()
                    elif options[selected] == "Sair":
                        pygame.quit()
                        sys.exit()


def key_config_menu():
    actions = list(key_bindings.keys())
    selected = 0

    while True:
        WIN.fill((245, 245, 245))
        pygame.draw.rect(WIN, (230, 230, 230), (80, 50, 640, 500), border_radius=15)

        title = font.render("Configurar Teclas", True, (40, 40, 40))
        subtitle = pygame.font.SysFont(None, 24).render("Use as Setas do teclado, ENTER para alterar, ESC para sair", True, (100, 100, 100))
        WIN.blit(title, (WIDTH//2 - title.get_width()//2, 60))
        WIN.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 100))

        for i, action in enumerate(actions):
            key_name = pygame.key.name(key_bindings[action])
            color = (0, 120, 255) if i == selected else (60, 60, 60)
            text = font.render(f"{action.upper()}: {key_name}", True, color)
            WIN.blit(text, (150, 150 + i * 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(actions)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(actions)
                elif event.key == pygame.K_RETURN:
                    waiting = True
                    while waiting:
                        for e in pygame.event.get():
                            if e.type == pygame.KEYDOWN:
                                key_bindings[actions[selected]] = e.key
                                waiting = False


FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PLAYER_SIZE = 50
BOSS_SIZE = 60
ROLL_SPEED = 8
WALK_SPEED = 4

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player_idle = pygame.image.load("assets/guerreiro.png").convert_alpha()
player_idle = pygame.transform.scale(player_idle, (51, 51))
player_roll = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player_roll.fill((0, 255, 255))

watcher_img = pygame.image.load("assets/boss1.png").convert_alpha()
watcher_img = pygame.transform.scale(watcher_img, (BOSS_SIZE, BOSS_SIZE))

fury_beast_img = pygame.image.load("assets/boss2.png").convert_alpha()
fury_beast_img = pygame.transform.scale(fury_beast_img, (BOSS_SIZE, BOSS_SIZE))

void_reaper_img = pygame.image.load("assets/boss3.png").convert_alpha()
void_reaper_img = pygame.transform.scale(void_reaper_img, (BOSS_SIZE, BOSS_SIZE))

projectile_image = pygame.Surface((10, 10))
projectile_image.fill((100, 0, 100))
player_attack_image = pygame.Surface((10, 40))
player_attack_image.fill((255, 200, 0))
attack_bar = pygame.Surface((200, 5))
attack_bar.fill(YELLOW)

def distribuir_pontos():
    attributes = {
        "Vida": 100,
        "Força": 10,
        "Armadura": 0,
        "Crítico": 0.1,
        "Vel. Ataque": 1.5
    }
    base_values = attributes.copy()
    options = list(attributes.keys())
    selected = 0
    points = 10

    # Cores
    BG_COLOR = (245, 245, 245)
    BOX_COLOR = (230, 230, 230)
    TEXT_COLOR = (30, 30, 30)
    SELECTED_COLOR = (0, 120, 220)
    BASE_COLOR = (50, 50, 50)
    REMAINING_COLOR = (100, 100, 100)

    while True:
        WIN.fill(BG_COLOR)
        pygame.draw.rect(WIN, BOX_COLOR, (100, 50, WIDTH - 200, HEIGHT - 100), border_radius=20)

        # Títulos
        title = font.render("Distribua seus Pontos", True, TEXT_COLOR)
        subtitle = pygame.font.SysFont(None, 24).render(
            "Use as SETAS para navegar | ENTER para confirmar", True, REMAINING_COLOR
        )

        WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, 70))
        WIN.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 110))

        # Atributos
        for i, key in enumerate(options):
            is_selected = i == selected
            color = SELECTED_COLOR if is_selected else BASE_COLOR
            value = attributes[key]
            base = base_values[key]
            display_text = f"{key:<12} | Base: {base} → Atual: {value}"
            attr_text = font.render(display_text, True, color)

            # Centralizado
            WIN.blit(attr_text, (WIDTH // 2 - attr_text.get_width() // 2, 160 + i * 50))

        # Pontos restantes
        points_text = font.render(f"Pontos restantes: {points}", True, REMAINING_COLOR)
        WIN.blit(points_text, (WIDTH // 2 - points_text.get_width() // 2, HEIGHT - 130))

        pygame.display.update()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RIGHT and points > 0:
                    attributes[options[selected]] += 1
                    points -= 1
                elif event.key == pygame.K_LEFT and attributes[options[selected]] > base_values[options[selected]]:
                    attributes[options[selected]] -= 1
                    points += 1
                elif event.key == pygame.K_RETURN and points == 0:
                    return attributes




class Player:
    def __init__(self, attrs):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT//2, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = WALK_SPEED
        self.hp = attrs["Vida"]
        self.max_hp = attrs["Vida"]
        self.strength = attrs["Força"]
        self.armor = attrs["Armadura"]
        self.crit = attrs["Crítico"]
        self.attack_speed = attrs["Vel. Ataque"]
        self.dodging = False
        self.dodge_timer = 0
        
        self.image = pygame.transform.scale(player_idle, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        self.last_attack = 0
        self.attack_visual_timer = 0

    def move(self, keys):
        dx = dy = 0
        if keys[key_bindings["up"]]: dy -= 1
        if keys[key_bindings["down"]]: dy += 1
        if keys[key_bindings["left"]]: dx -= 1
        if keys[key_bindings["right"]]: dx += 1

        if self.dodging:
            self.rect.x += dx * ROLL_SPEED
            self.rect.y += dy * ROLL_SPEED
        else:
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def dodge(self):
        self.dodging = True
        self.dodge_timer = pygame.time.get_ticks()
        self.image = player_roll

    def update(self):
        if self.dodging and pygame.time.get_ticks() - self.dodge_timer > 300:
            self.dodging = False
            self.image = player_idle

    def draw(self, win):
        win.blit(self.image, self.rect.topleft)

        # Animação de ataque (caso esteja atacando)
        if pygame.time.get_ticks() - self.attack_visual_timer < 150:
            win.blit(player_attack_image, (self.rect.centerx - 5, self.rect.top - 40))

        # Barra de vida
        pygame.draw.rect(win, RED, (10, 10, 200, 20))
        pygame.draw.rect(win, GREEN, (10, 10, 200 * (self.hp / self.max_hp), 20))

        # Barra de recarga de ataque
        time_since_attack = pygame.time.get_ticks() - self.last_attack
        cooldown = int(1500 / self.attack_speed)
        if time_since_attack < cooldown:
            pygame.draw.rect(win, YELLOW, (10, 35, 200 * (time_since_attack / cooldown), 5))
        else:
            pygame.draw.rect(win, YELLOW, (10, 35, 200, 5))

class Projectile:
    def __init__(self, x, y, dx, dy, speed, damage):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.dx = dx
        self.dy = dy
        self.speed = speed
        self.damage = damage
        self.image = projectile_image

    def move(self):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

    def draw(self, win):
        win.blit(self.image, self.rect.topleft)

class Boss:
    def __init__(self, x, y, hp, speed, name, dmg, image):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, BOSS_SIZE, BOSS_SIZE)
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.name = name
        self.damage = dmg
        self.alive = True
        self.image = image
        self.last_attack = 0
        self.projectiles = []

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    def move_towards_player(self, player):
        if not self.alive: return
        dx = dy = 0
        if player.rect.x > self.rect.x: dx = 1
        if player.rect.x < self.rect.x: dx = -1
        if player.rect.y > self.rect.y: dy = 1
        if player.rect.y < self.rect.y: dy = -1
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def ranged_attack(self, player):
        now = pygame.time.get_ticks()
        if now - self.last_attack > 1500:
            self.last_attack = now
            num_proj = random.randint(3, 7)
            for _ in range(num_proj):
                dx = player.rect.centerx - self.rect.centerx + random.randint(-50, 50)
                dy = player.rect.centery - self.rect.centery + random.randint(-50, 50)
                dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
                self.projectiles.append(Projectile(self.rect.centerx, self.rect.centery, dx / dist, dy / dist, 6, self.damage))

    def draw(self, win):
        if self.alive:
            win.blit(self.image, self.rect.topleft)
            pygame.draw.rect(win, RED, (WIDTH - 210, 10, 200, 20))
            pygame.draw.rect(win, GREEN, (WIDTH - 210, 10, 200 * (self.hp / self.max_hp), 20))
            text = font.render(self.name, True, BLACK)
            win.blit(text, (WIDTH - 210, 35))
            for proj in self.projectiles:
                proj.draw(win)

def boss_intro(boss):
    gate_rect = pygame.Rect(WIDTH // 2 - 50, -100, 100, 200)
    boss.rect.topleft = (WIDTH // 2 - BOSS_SIZE // 2, -BOSS_SIZE)
    name_surface = font.render(boss.name, True, RED)

    intro_timer = pygame.time.get_ticks()
    running = True
    while running:
        clock.tick(FPS)
        WIN.fill(BLACK)

        pygame.draw.rect(WIN, (80, 80, 80), gate_rect)

        if boss.rect.y < 150:
            boss.rect.y += 2
        else:
            WIN.blit(name_surface, (WIDTH // 2 - name_surface.get_width() // 2, HEIGHT // 2))
            if pygame.time.get_ticks() - intro_timer > 3500:
                running = False

        WIN.blit(boss.image, boss.rect.topleft)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
game_over = False
game_won = False


def main():
    while True:
        attrs = distribuir_pontos()
        player = Player(attrs)

        bosses = [
    Boss(0, 0, 40, 1, "Watcher", 5, watcher_img),
    Boss(0, 0, 70, 1.5, "Fury Beast", 10, fury_beast_img),
    Boss(0, 0, 120, 2, "Void Reaper", 15, void_reaper_img)
]

        current_boss = 0

        if current_boss < len(bosses):
            boss_intro(bosses[current_boss])

        game_over = False

        while not game_over:
            clock.tick(FPS)
            keys = pygame.key.get_pressed()
            now = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == key_bindings["dodge"]:
                    player.dodge()

            player.move(keys)
            player.update()

            if current_boss < len(bosses):
                boss = bosses[current_boss]
                boss.move_towards_player(player)
                boss.ranged_attack(player)

                for proj in boss.projectiles[:]:
                    proj.move()
                    if proj.rect.colliderect(player.rect) and not player.dodging:
                        player.hp -= max(0, proj.damage - player.armor)
                        boss.projectiles.remove(proj)

                if boss.alive and player.rect.colliderect(boss.rect):
                    cooldown = int(1500 / player.attack_speed)
                    if keys[key_bindings["attack"]] and now - player.last_attack > cooldown:
                        player.last_attack = now
                        player.attack_visual_timer = now
                        damage = player.strength
                        if random.random() < player.crit:
                            damage *= 2
                        boss.hp -= damage

                if boss.hp <= 0 and boss.alive:
                    boss.alive = False
                    current_boss += 1
                    if current_boss >= len(bosses):
                        end_screen("Você venceu todos os chefes!")
                        game_over = True
                    else:
                        boss_intro(bosses[current_boss])

            if player.hp <= 0:
                end_screen("Você morreu.")
                game_over = True

            WIN.fill(WHITE)
            player.draw(WIN)
            if current_boss < len(bosses):
                bosses[current_boss].draw(WIN)
            pygame.display.update()

        pygame.display.update()

def end_screen(mensagem):
    while True:
        WIN.fill(WHITE)
        
        # Texto de fim (vitória ou derrota)
        text = FONT.render(mensagem, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        WIN.blit(text, text_rect)

        # Botões
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Botão Voltar ao Menu
        menu_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        pygame.draw.rect(WIN, GRAY, menu_button)
        menu_text = FONT.render("Voltar ao Menu", True, BLACK)
        WIN.blit(menu_text, menu_text.get_rect(center=menu_button.center))

        # Botão Sair
        exit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50)
        pygame.draw.rect(WIN, GRAY, exit_button)
        exit_text = FONT.render("Sair do Jogo", True, BLACK)
        WIN.blit(exit_text, exit_text.get_rect(center=exit_button.center))

        pygame.display.update()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu_button.collidepoint(mouse_pos):
                    main_menu()
                    return
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()





if __name__ == "__main__":
    main_menu()
    main()