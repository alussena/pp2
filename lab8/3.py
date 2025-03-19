import pygame
import random
import time

pygame.init() # initializes all the pygame sub-modules

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # creating a game window
# set_mode() takes a tuple as an argument

background = pygame.image.load('AnimatedStreet.png')

running = True

# this object allows us to set the FPS
clock = pygame.time.Clock()
FPS = 60 

player_img = pygame.image.load('Player.png')
enemy_img = pygame.image.load('Enemy.png')
coin_img = pygame.image.load('Coin.png')
coin_img = pygame.transform.scale(coin_img, (30, 30)) 


background_music = pygame.mixer.music.load('background.wav')
crash_sound = pygame.mixer.Sound('crash.wav')

font = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, "black")

pygame.mixer.music.play(-1) # plays background music in a loop

PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = 5
score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0) # move in place
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0) # move in place
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
    
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = 0

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.generate_random_position()

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_position()

    def generate_random_position(self):
        self.rect.x = random.randint(0, max(0, WIDTH - self.rect.w))
        self.rect.y = random.randint(50, max(50, HEIGHT - self.rect.h))


player = Player() # player's sprite
enemy = Enemy() # enemy's sprite
coin = Coin() # coin's sprite

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, coin)
enemy_sprites.add([enemy])
coin_sprites.add([coin])


def draw_score():
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (10, 10)) 


while running: # game loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))

    player.move()
    enemy.move()
    coin.move()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)

        screen.fill("red")
        center_rect = game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)

        pygame.display.flip()

        time.sleep(2)
        running = False

    if pygame.sprite.spritecollideany(player, coin_sprites):
        score += 1
        coin.kill()
        coin = Coin()
        all_sprites.add(coin)
        coin_sprites.add(coin)


    draw_score()
    pygame.display.flip() # updates the screen
    clock.tick(FPS) # sets the FPS

pygame.quit()