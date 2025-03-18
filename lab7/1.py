import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


background = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png") 
sec_hand = pygame.image.load("sec_hand.png") 

center = (300,300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    
    min_angle = -(minutes*6) +90
    sec_angle = -(seconds*6) +90
    

    rotated_min = pygame.transform.rotate(min_hand, min_angle)
    rotated_sec = pygame.transform.rotate(sec_hand, sec_angle)

    new_min_rect = rotated_min.get_rect(center=center)
    new_sec_rect = rotated_sec.get_rect(center=center)


    screen.fill((255, 255, 255))
    screen.blit(background, background.get_rect(center=center))
    screen.blit(rotated_min, new_min_rect)
    screen.blit(rotated_sec, new_sec_rect)
    
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()