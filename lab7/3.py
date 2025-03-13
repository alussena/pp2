import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((500, 500))

COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
move_step = 20
FPS = 60
is_red = True
clock = pygame.time.Clock()
running = True

while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP] and circle_y - move_step >= 0:
        circle_y -= move_step
    if pressed_keys[pygame.K_DOWN] and circle_y + move_step <= HEIGHT:
        circle_y += move_step
    if pressed_keys[pygame.K_RIGHT] and circle_x + move_step <= WIDTH:
        circle_x += move_step
    if pressed_keys[pygame.K_LEFT] and circle_x - move_step >= 0:
        circle_x -= move_step

    if is_red:
        screen.fill(COLOR_RED)
        pygame.draw.circle(screen, COLOR_BLUE, (circle_x, circle_y), 25)
    else:
        screen.fill(COLOR_BLUE)
        pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), 25)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
