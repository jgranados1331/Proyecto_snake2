import pygame
import random

class Configuraciones(object):
    def __init__(self):
        
        #Pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.game_window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.name_game = "Snake Game 2"
        self.icon=pygame.image.load("Images/Incono.png")
        self.background_game = pygame.image.load("Images/INTRO.jpg")

        #Comida
        self.apple = pygame.image.load("Images/apple.png")
        self.chocolate = pygame.image.load("Images/chocolateg.png")
        self.mouse = pygame.image.load("Images/mouse.png")
        self.select_food=random.randint(0,2)
        self.food_positionx = random.randint(70,1110)
        self.food_positiony = random.randint(50,730)
        self.food_spawn = True

        #Paredes
        self.pared_ancha = pygame.image.load("Images/pared_ancha.png")
        self.pared_alta = pygame.image.load("Images/pared_larga.png")

        #Snake y dirección de la serpiente
        self.cabeza = pygame.image.load("Images/cabeza.png")
        self.direction = 'RIGHT'
        self.cambiar_a = self.direction
        self.snake_1_position = [100, 50]

        #Players
        self.velocity_factor_player1=1
        
        self.velocity_factor_player2=1

        

        