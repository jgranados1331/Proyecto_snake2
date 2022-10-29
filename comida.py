import pygame 
from configuraciones import Configuraciones

class Comida(self):
    ai_configuraciones=Configuraciones
    def __init__(self, ai_configuraciones,pantalla, nave):
        self.pantalla = pantalla
        

        comida=[ai_configuraciones.apple,ai_configuraciones.chocolate,ai_configuraciones.mouse]

        self.rect = pygame.Rect(0,0)
        self.comida=comida[ai_configuraciones.select_food]

    def draw_food(self):
        self.pantalla.blit(self.comida, self.rect)

