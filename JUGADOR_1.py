import pygame
import random
from pygame.sprite import Sprite
from configuraciones import Configuraciones
from comida import Comida
from paredes import pared
from game_functions import game_over



class serpiente_1(Sprite):
    """Comportamiento de la primera serpiente"""

    def __init__(self, ai_configuraciones, pantalla):
        """Inicia la serpiente y la posicion de partida"""
        super(serpiente_1, self).__init__()
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Imagen de la serpiente
        color_serpiente = (0, 0, 255)
        self.image = pygame.draw.rect(pantalla, color_serpiente, [200, 150, 10, 10])
        self.pantalla_rect = pantalla.get_rect()

        # Cuerpo de la primera serpiente
        self.snake_body = [[100, 50],
                            [90, 50],
                            [80, 50],
                            [70, 50]
                            ]

        # Almacena un valor decimal para el centro de la serpiente
        self.position = self.snake_body
        self.update()


def update(self):
    """Actualiza la posicion de la nave segun las banderas de movimiento"""
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    wall = pared(ai_configuraciones, pantalla)
    #Teclado cuando se mantienen presionadas teclas
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ai_configuraciones.cambiar_a = 'UP'
                
            if event.key == pygame.K_s:
                ai_configuraciones.cambiar_a = 'DOWN'
                
            if event.key == pygame.K_a:
                ai_configuraciones.cambiar_a = 'LEFT'
                
            if event.key == pygame.K_d:
                ai_configuraciones.cambiar_a = 'RIGHT'
                
    
    # Condiciones para el teclado
    if ai_configuraciones.cambiar_a == 'UP' and ai_configuraciones.direction != 'DOWN':
        ai_configuraciones.direction = 'UP'
    if ai_configuraciones.cambiar_a == 'DOWN' and ai_configuraciones.direction != 'DOWN':
        ai_configuraciones.direction = 'DOWN'
    if ai_configuraciones.cambiar_a == 'LEFT' and ai_configuraciones.direction != 'RIGHT':
        ai_configuraciones.direction = 'LEFT'
    if ai_configuraciones.cambiar_a == 'RIGHT' and ai_configuraciones.direction != 'LEFT':
        ai_configuraciones.direction = 'RIGHT'

    # Movimiento de la serpiente
    if ai_configuraciones.direction == 'UP':
        ai_configuraciones.snake_1_position[1] -= 10
    if ai_configuraciones.direction == 'DOWN':
        ai_configuraciones.snake_1_position[1] += 10
    if ai_configuraciones.direction == 'LEFT':
        ai_configuraciones.snake_1_position[0] -= 10
    if ai_configuraciones.direction == 'RIGHT':
        ai_configuraciones.snake_1_position[0] += 10

    # Condiciones para morir:
    # Si toca la pared
    if self.position == wall.rect or wall.rects:
        game_over()
    if self.position == wall.rectizq or wall.rectder:
        game_over()
    # Si toca el propio cuerpo
    for block in self.snake_body[1:]:
        if self.position[0] == block [0] and self.position[1] == block[1]:
            game_over()
            

def comida_crecimiento (self):
    """Crecimiento de la serpiente, si se come la fruta, incrementa en 10 su tamaño"""
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    food = Comida(ai_configuraciones, pantalla)
    self.snake_body.insert(0, list(ai_configuraciones.snake_1_position))
    if ai_configuraciones.snake_1_position[0] == ai_configuraciones.food_positionx and ai_configuraciones.snake_1_position[1] == ai_configuraciones.food_positiony: 
        if food.comida == ai_configuraciones.apple:
            # Aqui colocar que el puntaje incrementa en 10
            ai_configuraciones.food_spawn = False
        elif food.comida == ai_configuraciones.chocolate:
            # Aqui colocar que el puntaje se incrementa en 15
            ai_configuraciones.food_spawn = False
        else:
            #Aqui colocar que el puntaje se incrementa en 20
            ai_configuraciones.food_spawn = False

    else:
        self.snake_body.pop()
    
    if not ai_configuraciones.food_spawn:
        ai_configuraciones.food_positionx = random.randint(70, 1110)
        ai_configuraciones.food_positiony = random.randint(50, 730)

    ai_configuraciones.food_spawn = True

    for pos in self.snake_body:
        pygame.draw.rect(ai_configuraciones.game_window, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(ai_configuraciones.game_window, (255, 255, 255), pygame.Rect(food.rect[0], food.rect[1], 10, 10))

    # Refrescar la pantalla
    pygame.display.update()




        


