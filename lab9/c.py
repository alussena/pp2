import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)     # Красная 3 балла
colorGREEN = (0, 255, 0)   # Зелёная 2 балла

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x >= WIDTH // CELL:
            self.body[0].x = 0
        if self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        if self.body[0].y >= HEIGHT // CELL:
            self.body[0].y = 0
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorWHITE, (segment.x * CELL, segment.y * CELL, CELL, CELL))

class Food:
    def __init__(self):
        self.generate_random_pos()

    def generate_random_pos(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.color = colorRED if random.random() < 0.2 else colorGREEN  # 20% шанс красной еды
        self.weight = 3 if self.color == colorRED else 2 
        self.time_created = time.time()  # Засекаем время появления еды

    def update(self):
        if time.time() - self.time_created > 7:  #если прошло 7 секунд, обновляем еду
            self.generate_random_pos()

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

def check_collision(snake, food):
    global score, level, FPS
    if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
        score += food.weight
        snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
        food.generate_random_pos()

        if score % 5 == 0:
            level += 1

def draw_score():
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))

FPS = 7
clock = pygame.time.Clock()
score = 0
level = 1

snake = Snake()
food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)

    snake.move()
    check_collision(snake, food)
    food.update()  #исчзенет ли еда

    snake.draw()
    food.draw()
    draw_score()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
