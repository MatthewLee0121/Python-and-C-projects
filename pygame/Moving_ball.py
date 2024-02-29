import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
bullets = []

class Enemy:
    def __init__(self, pos, direction):
        self.pos = pygame.Vector2(pos)
        self.direction = pygame.Vector2(direction)
        self.speed = 200

    def update(self, dt):
        self.pos += self.direction * self.speed * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.pos, 20)

class Bullet:
    def __init__(self, pos, direction):
        self.pos = pygame.Vector2(pos)
        self.direction = pygame.Vector2(direction)
        self.speed = 800 

    def update(self, dt):
        self.pos += self.direction * self.speed * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                direction = pygame.Vector2(pygame.mouse.get_pos()) - player_pos
                direction.normalize_ip()
                bullets.append(Bullet(player_pos, direction))

    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    for bullet in bullets:
        bullet.update(dt)
        bullet.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
