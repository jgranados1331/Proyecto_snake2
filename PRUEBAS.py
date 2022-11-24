# importing libraries
import pygame
import time
import random
from configuraciones import Configuraciones
from paredes import pared

wall = pared
# FONDO
bg = pygame.image.load("Images/INTRO.jpg")
# PAREDES
ancho = pygame.image.load("Images/pared_ancha.png")
altura = pygame.image.load("Images/pared_larga.png")



snake_speed = 15
ganador = ""
# Window size
window_x = 1200
window_y = 800
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
orange = pygame.Color(255, 127, 0)
yellow = pygame.Color(255, 255, 0)
 
# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake II')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position_1 = [100, 350]
snake_position_2 = [1100, 350]
 
# defining first 4 blocks of snake body
snake_body_1 = [[100, 350],
              [90, 350],
              [80, 350],
              [70, 350]
              ]

snake_body_2 = [[500, 350],
                [490, 350],
                [480, 350],
                [470, 350]
                ]
a = 0
b = 0
for x in snake_body_1:
    a += 1
for y in snake_body_2:
    b += 1
# POSICIÓN DE LAS FRUTAS
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# FRUTAS SELECCIONABLES
apple = pygame.image.load("Images/apple.png").convert()
chocolate = pygame.image.load("Images/chocolateg.png").convert()
mouse = pygame.image.load("Images/mouse.png").convert()


# setting default snake direction towards
# right

direction_1 = 'RIGHT'
change_to_1 = direction_1
direction_2 = 'LEFT'
change_to_2 = direction_2 
# initial score
score_1 = 0
score_2 = 0
# displaying Score function
def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Jugador 1: ' + str(score_1), True, color)
    score_surface_2 = score_font.render('Jugador 2: ' + str(score_2), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    score_rect_2 = score_surface_2.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
    game_window.blit(score_surface_2,(900,0), score_rect_2)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    surface = pygame.Surface((1000, 50))
    surface.fill('Red')
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'El ganador es: ' + str(ganador) + "Con un puntaje de: " + str(score_1), True, white)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(surface,(125, window_y/4))
    game_window.blit(game_over_surface, game_over_rect)
    
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 
 
# Main Function
while True:
    game_window.blit(bg, (0,0))
    game_window.blit(ancho, (0, 735))
    game_window.blit(ancho, (0,0))
    game_window.blit(altura, (0, 0))
    game_window.blit(altura, (1150, 0))
    
    # Refresh game screen
    
    for x in snake_body_1:
        a += 1
    for y in snake_body_2:
        b += 1 
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to_1 = 'UP'
                
            if event.key == pygame.K_s:
                change_to_1 = 'DOWN'
                
            if event.key == pygame.K_a:
                change_to_1 = 'LEFT'
                
            if event.key == pygame.K_d:
                change_to_1 = 'RIGHT'
                
            if event.key == pygame.K_UP:
                change_to_2 = 'UP'
                
            if event.key == pygame.K_DOWN:
                change_to_2 = 'DOWN'
                
            if event.key == pygame.K_LEFT:
                change_to_2 = 'LEFT'
                
            if event.key == pygame.K_RIGHT:
                change_to_2 = 'RIGHT'
                
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to_1 == 'UP' and direction_1 != 'DOWN':
        direction_1 = 'UP'
        
    if change_to_1 == 'DOWN' and direction_1 != 'UP':
        direction_1 = 'DOWN'
        
        
    if change_to_1 == 'LEFT' and direction_1 != 'RIGHT':
        direction_1 = 'LEFT'
        
        
    if change_to_1 == 'RIGHT' and direction_1 != 'LEFT':
        direction_1 = 'RIGHT'
        

    if change_to_2 == 'UP' and direction_2 != 'DOWN':
        direction_2 = 'UP'
        
    if change_to_2 == 'DOWN' and direction_2 != 'UP':
        direction_2 = 'DOWN'
        
        
    if change_to_2 == 'LEFT' and direction_2 != 'RIGHT':
        direction_2 = 'LEFT'
        
        
    if change_to_2 == 'RIGHT' and direction_2 != 'LEFT':
        direction_2 = 'RIGHT'
        
        
 
    # Moving the snake
    if direction_1 == 'UP':
        snake_position_1[1] -= 10
        
    if direction_1 == 'DOWN':
        snake_position_1[1] += 10
        
    if direction_1 == 'LEFT':
        snake_position_1[0] -= 10
        
    if direction_1 == 'RIGHT':
        snake_position_1[0] += 10
        
 
    if direction_2 == 'UP':
        snake_position_2[1] -= 10
        
    if direction_2 == 'DOWN':
        snake_position_2[1] += 10
        
    if direction_2 == 'LEFT':
        snake_position_2[0] -= 10
        
    if direction_2 == 'RIGHT':
        snake_position_2[0] += 10
        

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body_1.insert(0, list(snake_position_1))
    if snake_position_1[0] == fruit_position[0] and snake_position_1[1] == fruit_position[1]:
        score_1 += 10
        fruit_spawn = False
    else:
        snake_body_1.pop()

    snake_body_2.insert(0, list(snake_position_2))
    if snake_position_2[0] == fruit_position[0] and snake_position_2[1] == fruit_position[1]:
        score_2 += 10
        fruit_spawn = False
    else:
        snake_body_2.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 20,
                          random.randrange(1, (window_y//10)) * 20]
         
    fruit_spawn = True
    
     
    for pos in snake_body_1:
        pygame.draw.rect(game_window, orange,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    for pos1 in snake_body_2:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos1[0], pos1[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

 
    # COLISIONES 
    if snake_position_1[0] in (50, 1150):
        ganador = "Jugador 2"
        game_over()
    if snake_position_1[1] in (50, 730):
        ganador = "Jugador 2"
        game_over()
    
    if snake_position_2[0] in (50, 1150):
        ganador = "Jugador 1"
        game_over()
    if snake_position_2[1] in (50, 730):
        ganador = "jugador 1"
        game_over()
 
    # COLISIONES ENTRE CUERPOS
    if snake_body_1[0] == snake_body_2[0]:
        ganador = "Jugador 2"
        game_over()
    if snake_body_2[0] == snake_body_1[0]:
        ganador = "Jugador 1"
        game_over()
    
    

 
    # displaying score countinuously
    show_score(1, red, 'comic sans', 40)
    pygame.display.update()
    
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)

# EJECUTA TODAS LAS PAREDES