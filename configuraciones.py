import pygame

class Configuraciones(object):
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.name_game = "Snake Game 2"
        self.icon=pygame.image.load("Images/Incono.png")
        self.background_game = pygame.image.load("Images/background.png")
    

        self.velocity_factor_player1=1
        
        self.velocity_factor_player2=1
        