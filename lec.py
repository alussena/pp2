# import pygame

# pygame.init()

# WIDTH = 800
# HEIGHT = 600

# screen = pygame.display.set_mode((WIDTH, HEIGHT))

# colorRED = (255, 0, 0)
# colorBLUE = (0, 0, 255)
# colorWHITE = (255, 255, 255)
# colorBLACK = (0, 0, 0)

# LMBpressed = False
# THICKNESS = 5

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             print("LMB pressed!")
#             LMBpressed = True
#         if event.type == pygame.MOUSEMOTION:
#             print("Position of the mouse:", event.pos)
#             if LMBpressed:
#                 pygame.draw.rect(screen, colorRED, (event.pos[0], event.pos[1], THICKNESS, THICKNESS))
#         if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#             print("LMB released!")
#             LMBpressed = False
#         if event.type == pygame.KEYDOWN: 
#             if event.key == pygame.K_EQUALS:
#                 print("increased thickness")
#                 THICKNESS += 1
#             if event.key == pygame.K_MINUS:
#                 print("reduced thickness")
#                 THICKNESS -= 1
    
#     pygame.display.flip()

# 

# import pygame

# class SceneBase:
#     def __init__(self):
#         self.next = self
    
#     def ProcessInput(self, events, pressed_keys):
#         print("uh-oh, you didn't override this in the child class")

#     def Update(self):
#         print("uh-oh, you didn't override this in the child class")

#     def Render(self, screen):
#         print("uh-oh, you didn't override this in the child class")

#     def SwitchToScene(self, next_scene):
#         self.next = next_scene
    
#     def Terminate(self):
#         self.SwitchToScene(None)

# def run_game(width, height, fps, starting_scene):
#     pygame.init()
#     screen = pygame.display.set_mode((width, height))
#     clock = pygame.time.Clock()

#     active_scene = starting_scene

#     while active_scene != None:
#         pressed_keys = pygame.key.get_pressed()
        
#         # Event filtering
#         filtered_events = []
#         for event in pygame.event.get():
#             quit_attempt = False
#             if event.type == pygame.QUIT:
#                 quit_attempt = True
#             elif event.type == pygame.KEYDOWN:
#                 alt_pressed = pressed_keys[pygame.K_LALT] or \
#                               pressed_keys[pygame.K_RALT]
#                 if event.key == pygame.K_ESCAPE:
#                     quit_attempt = True
#                 elif event.key == pygame.K_F4 and alt_pressed:
#                     quit_attempt = True
            
#             if quit_attempt:
#                 active_scene.Terminate()
#             else:
#                 filtered_events.append(event)
        
#         active_scene.ProcessInput(filtered_events, pressed_keys)
#         active_scene.Update()
#         active_scene.Render(screen)
        
#         active_scene = active_scene.next
        
#         pygame.display.flip()
#         clock.tick(fps)

# # The rest is code where you implement your game using the Scenes model

# class TitleScene(SceneBase):
#     def __init__(self):
#         SceneBase.__init__(self)
    
#     def ProcessInput(self, events, pressed_keys):
#         for event in events:
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
#                 # Move to the next scene when the user pressed Enter
#                 self.SwitchToScene(GameScene())
    
#     def Update(self):
#         pass
    
#     def Render(self, screen):
#         # For the sake of brevity, the title scene is a blank red screen
#         screen.fill((255, 0, 0))

# class GameScene(SceneBase):
#     def __init__(self):
#         SceneBase.__init__(self)
    
#     def ProcessInput(self, events, pressed_keys):
#         pass
        
#     def Update(self):
#         pass
    
#     def Render(self, screen):
#         # The game scene is just a blank blue screen
#         screen.fill((0, 0, 255))

# run_game(400, 300, 60, TitleScene())

# import pygame

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((640, 480))
#     clock = pygame.time.Clock()
    
#     radius = 15
#     x = 0
#     y = 0
#     mode = 'blue'
#     points = []
    
#     while True:
        
#         pressed = pygame.key.get_pressed()
        
#         alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
#         ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
#         for event in pygame.event.get():
            
#             # determin if X was clicked, or Ctrl+W or Alt+F4 was used
#             if event.type == pygame.QUIT:
#                 return
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_w and ctrl_held:
#                     return
#                 if event.key == pygame.K_F4 and alt_held:
#                     return
#                 if event.key == pygame.K_ESCAPE:
#                     return
            
#                 # determine if a letter key was pressed
#                 if event.key == pygame.K_r:
#                     mode = 'red'
#                 elif event.key == pygame.K_g:
#                     mode = 'green'
#                 elif event.key == pygame.K_b:
#                     mode = 'blue'
            
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1: # left click grows radius
#                     radius = min(200, radius + 1)
#                 elif event.button == 3: # right click shrinks radius
#                     radius = max(1, radius - 1)
            
#             if event.type == pygame.MOUSEMOTION:
#                 # if mouse moved, add point to list
#                 position = event.pos
#                 points = points + [position]
#                 points = points[-256:]
                
#         screen.fill((0, 0, 0))
        
#         # draw all points
#         i = 0
#         while i < len(points) - 1:
#             drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
#             i += 1
        
#         pygame.display.flip()
        
#         clock.tick(60)

# def drawLineBetween(screen, index, start, end, width, color_mode):
#     c1 = max(0, min(255, 2 * index - 256))
#     c2 = max(0, min(255, 2 * index))
    
#     if color_mode == 'blue':
#         color = (c1, c1, c2)
#     elif color_mode == 'red':
#         color = (c2, c1, c1)
#     elif color_mode == 'green':
#         color = (c1, c2, c1)
    
#     dx = start[0] - end[0]
#     dy = start[1] - end[1]
#     iterations = max(abs(dx), abs(dy))
    
#     for i in range(iterations):
#         progress = 1.0 * i / iterations
#         aprogress = 1 - progress
#         x = int(aprogress * start[0] + progress * end[0])
#         y = int(aprogress * start[1] + progress * end[1])
#         pygame.draw.circle(screen, color, (x, y), width)

# main()