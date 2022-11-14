import pygame 
from configuraciones import Configuraciones

class Comida():
    ai_configuraciones=Configuraciones
    def __init__(self, ai_configuraciones,pantalla):
        self.pantalla = pantalla
        self.ia_configuraciones = ai_configuraciones
        

        comida=[ai_configuraciones.apple,ai_configuraciones.chocolate,ai_configuraciones.mouse,ai_configuraciones.burger,ai_configuraciones.mango,ai_configuraciones.pizza,ai_configuraciones.coca]
        #comida 1
        self.comida=comida[ai_configuraciones.select_food]
        self.rect = self.comida.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        self.rect.centerx = ai_configuraciones.food_positionx
        self.rect.centery = ai_configuraciones.food_positiony
        #comida 2
        self.comida2=comida[ai_configuraciones.select_food2]
        self.rect2 = self.comida.get_rect()
        self.pantalla_rect2 = pantalla.get_rect()
        self.rect2.centerx = ai_configuraciones.food2_positionx
        self.rect2.centery = ai_configuraciones.food2_positiony


    def blitme(self):
        self.pantalla.blit(self.comida, self.rect)
        self.pantalla.blit(self.comida2, self.rect2)

