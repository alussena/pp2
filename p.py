import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

CELL = 30

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

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

        # checks the right border
        if self.body[0].x > WIDTH // CELL - 1:
            self.body[0].x = 0
        # checks the left border
        if self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL - 1:
            self.body[0].y = 0
        # checks the top border
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1


    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos()

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, WIDTH // CELL - 1)
        self.pos.y = random.randint(0, HEIGHT // CELL - 1)



FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

score = 0
level = 1

# Отображение счета и уровня
def draw_score():
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))

# Модифицированный метод генерации еды, чтобы не появляться на змее
def generate_food(snake):
    while True:
        x = random.randint(0, WIDTH // CELL - 1)
        y = random.randint(0, HEIGHT // CELL - 1)
        if not any(segment.x == x and segment.y == y for segment in snake.body):
            return Point(x, y)

# Обновленный check_collision для обработки очков, уровня и скорости
def check_collision(snake, food):
    global score, level, FPS
    if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
        score += 1
        snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
        food.pos = generate_food(snake)

        if score % 3 == 0:
            level += 1
            FPS += 2

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
    draw_grid()

    snake.move()
    check_collision(snake, food)

    snake.draw()
    food.draw()
    draw_score()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
