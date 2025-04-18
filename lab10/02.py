import pygame
import random
import time
import psycopg2

conn = psycopg2.connect(
    dbname="Snake", 
    user="postgres", 
    password="12345678", 
    host="localhost", 
    port="5432"
)
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_scores (
        username VARCHAR(50) PRIMARY KEY,
        score INTEGER NOT NULL,
        level INTEGER NOT NULL
    );
""")
conn.commit()


pygame.init()
WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont(None, 36)

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)

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
        self.body[0].x %= WIDTH // CELL
        self.body[0].y %= HEIGHT // CELL

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorWHITE, (segment.x * CELL, segment.y * CELL, CELL, CELL))

class Food:
    def __init__(self):
        self.generate_random_pos()

    def generate_random_pos(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.color = colorRED if random.random() < 0.2 else colorGREEN
        self.weight = 3 if self.color == colorRED else 2
        self.time_created = time.time()

    def update(self):
        if time.time() - self.time_created > 7:
            self.generate_random_pos()

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

def check_collision(snake, food):
    global score, level
    if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
        score += food.weight
        snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
        food.generate_random_pos()
        if score % 5 == 0:
            level += 1

def draw_score():
    score_text = font.render(f"Score: {score}  Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))

def get_user_score(username):
    cursor.execute("SELECT score, level FROM user_scores WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        cursor.execute("INSERT INTO user_scores (username, score, level) VALUES (%s, %s, %s)", (username, 0, 1))
        conn.commit()
        return (0, 1)



def save_user_score(username, score, level):
    try:
        # Отладочная печать для вывода данных перед запросом
        print(f"Saving score for {username}: score={score}, level={level}")
        
        cursor.execute("""
            INSERT INTO user_scores (username, score, level)
            VALUES (%s, %s, %s)
            ON CONFLICT (username) 
            DO UPDATE SET score = GREATEST(user_scores.score, %s), level = %s
        """, (username, score, level, score, level))
        
        # Принудительный commit
        conn.commit()
        
        # Выводим успешное сообщение
        print(f"Score for {username} saved/updated successfully.")
        
        # Проверяем изменения в базе данных
        cursor.execute("SELECT * FROM user_scores;")
        rows = cursor.fetchall()
        print("Current data in user_scores table:")
        for row in rows:
            print(row)
            
    except Exception as e:
        print(f"Error while saving user score: {e}")
        conn.rollback()






def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, colorGRAY, (x, y, w, h))
    label = font.render(text, True, colorBLACK)
    screen.blit(label, (x + 10, y + 10))

def username_input_screen():
    username_input = ""
    input_active = True
    while input_active:
        screen.fill(colorBLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username_input != "":
                    return username_input
                elif event.key == pygame.K_BACKSPACE:
                    username_input = username_input[:-1]
                else:
                    username_input += event.unicode
        input_box = font.render("Enter Username: " + username_input, True, colorWHITE)
        screen.blit(input_box, (WIDTH // 4, HEIGHT // 2))
        pygame.display.flip()

def welcome_screen(username, score, level):
    waiting = True
    while waiting:
        screen.fill(colorBLACK)
        welcome_text = font.render(f"Welcome, {username}!", True, colorWHITE)
        score_text = font.render(f"Previous Score: {score} | Level: {level}", True, colorWHITE)
        instruction_text = font.render("Press SPACE to start the game", True, colorGREEN)
        screen.blit(welcome_text, (WIDTH // 4, HEIGHT // 3))
        screen.blit(score_text, (WIDTH // 4, HEIGHT // 3 + 40))
        screen.blit(instruction_text, (WIDTH // 4, HEIGHT // 3 + 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

username = username_input_screen()
score, level = get_user_score(username)
welcome_screen(username, score, level)

FPS = 7
snake = Snake()
food = Food()
clock = pygame.time.Clock()
paused = False
running = True

while running:
    screen.fill(colorBLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_user_score(username, score, level)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if WIDTH - 120 <= mouse_pos[0] <= WIDTH - 20 and 10 <= mouse_pos[1] <= 50:
                paused = not paused
                save_user_score(username, score, level)

    if not paused:
        snake.move()
        check_collision(snake, food)
        food.update()

    snake.draw()
    food.draw()
    draw_score()
    draw_button("Pause", WIDTH - 120, 10, 100, 40)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
