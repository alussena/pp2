import pygame

pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLUE

radius = 5 
mode = "pen"  
start_pos = None
is_drawing = False
points = []

screen.fill(BLACK)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #смена цветов
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            #режимы рисования
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_t:
                mode = "rect"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_1:
                mode = "right_triangle"
            elif event.key == pygame.K_2:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_3:
                mode = "rhombus"
            #рег размера кисти
            elif event.key == pygame.K_EQUALS:
                radius = min(50, radius + 1)
            elif event.key == pygame.K_MINUS:
                radius = max(1, radius - 1)
            elif event.key == pygame.K_ESCAPE:
                screen.fill(BLACK)
                pygame.display.flip()

        #нажатие 
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            is_drawing = True
            if mode == "pen":
                points.append(event.pos)
        #отпускание
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            is_drawing = False
            #прямоугольник
            if mode == "rect":
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                   abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)
            #квадрат
            elif mode == "square":
                side = min(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                pygame.draw.rect(screen, current_color, rect, 2)
            #круг
            elif mode == "circle":
                center = start_pos
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, center, radius, 2)
            #прямоугольный треугольник
            elif mode == "right_triangle":
                pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            #равносторонний треугольник
            elif mode == "equilateral_triangle":
                height = abs(start_pos[1] - end_pos[1])
                base = height * (3 ** 0.5) / 2
                pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0] + base, start_pos[1] + height),
                                                            (start_pos[0] - base, start_pos[1] + height)], 2)
                #drawing rhombus
            elif mode == "rhombus":
                dx = abs(start_pos[0] - end_pos[0])
                dy = abs(start_pos[1] - end_pos[1])
                pygame.draw.polygon(screen, current_color, [(start_pos[0], start_pos[1] - dy),
                                                            (start_pos[0] + dx, start_pos[1]),
                                                            (start_pos[0], start_pos[1] + dy),
                                                            (start_pos[0] - dx, start_pos[1])], 2)
            pygame.display.flip()

        if event.type == pygame.MOUSEMOTION and is_drawing:
            if mode == "pen":
                pygame.draw.line(screen, current_color, points[-1], event.pos, radius)
                points.append(event.pos)
            elif mode == "eraser":
                pygame.draw.circle(screen, BLACK, event.pos, radius)
            pygame.display.flip()

    clock.tick(60)

pygame.quit()
