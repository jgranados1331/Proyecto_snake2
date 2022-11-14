import pygame 
from configuraciones import Configuraciones

class Comida():
    ai_configuraciones=Configuraciones
    def __init__(self, ai_configuraciones,pantalla):
        self.pantalla = pantalla
        self.ia_configuraciones = ai_configuraciones
        

        comida=[ai_configuraciones.apple,ai_configuraciones.chocolate,ai_configuraciones.mouse]
        self.comida=comida[ai_configuraciones.select_food]
        self.rect = self.comida.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        self.rect.centerx = ai_configuraciones.food_positionx
        self.rect.centery = ai_configuraciones.food_positiony

    def blitme(self):
        self.pantalla.blit(self.comida, self.rect)

