import pygame
import random

class Configuraciones(object):
    def __init__(self):
        
        #Pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.name_game = "Snake Game 2"
        self.icon=pygame.image.load("Images/Incono.png")
        self.background_game = pygame.image.load("Images/pasto.jpg")
        self.image_background = pygame.image.load("Images/INTRO.jpg")

        #Comida
        self.apple = pygame.image.load("Images/apple.png")
        self.chocolate = pygame.image.load("Images/chocolateg.png")
        self.mouse = pygame.image.load("Images/raton.png")
        self.burger = pygame.image.load("Images/hambur.png")
        self.mango = pygame.image.load("Images/mango.png")
        self.pizza = pygame.image.load("Images/pizza.png")
        self.coca = pygame.image.load("Images/coca.png")
        self.select_food=random.randint(0,6)
        self.select_food2=random.randint(0,6)
        self.food_positionx = random.randint(70,1110)
        self.food_positiony = random.randint(55,730)
        self.food2_positionx = random.randint(70,1110)
        self.food2_positiony = random.randint(55,730)

        #Paredes
        self.pared_ancha = pygame.image.load("Images/pared_ancha.png")
        self.pared_alta = pygame.image.load("Images/pared_larga.png")

        #Snake
        self.cabeza = pygame.image.load("Images/cabeza.png")

        #Players
        self.velocity_factor_player1=1
        self.velocity_factor_player2=1
        