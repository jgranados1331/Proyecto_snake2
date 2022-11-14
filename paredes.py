import pygame 
from configuraciones import Configuraciones

class pared():
    ai_configuraciones=Configuraciones
    def __init__(self, ai_configuraciones,pantalla):
        self.pantalla = pantalla
        self.ia_configuraciones = ai_configuraciones
        
        #Pared inferior
        self.pared_ancha_1 = ai_configuraciones.pared_ancha
        self.rect = self.pared_ancha_1.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.centery = self.pantalla_rect.centery
        self.rect.bottom = self.pantalla_rect.bottom
        ##Pared superior
        self.pared_ancha_2 = ai_configuraciones.pared_ancha
        self.rects = self.pared_ancha_2.get_rect()
        self.pantalla_rects = pantalla.get_rect()
        self.rects.centerx = self.pantalla_rect.centerx
        self.rects.centery = self.pantalla_rect.centery
        self.rects.top = self.pantalla_rect.top
        #Pared lateral izq
        self.pared_alta_izq = ai_configuraciones.pared_alta
        self.rectizq = self.pared_alta_izq.get_rect()
        self.pantalla_rectizq = pantalla.get_rect()
        self.rectizq.centerx = self.pantalla_rect.centerx
        self.rectizq.centery = self.pantalla_rect.centery
        self.rectizq.left = self.pantalla_rect.left
        self.rectizq.top = self.pantalla_rect.top
        #pared lateral der
        self.pared_alta_der = ai_configuraciones.pared_alta
        self.rectder = self.pared_alta_der.get_rect()
        self.pantalla_rectder = pantalla.get_rect()
        self.rectder.centerx = self.pantalla_rect.centerx
        self.rectder.centery = self.pantalla_rect.centery
        self.rectder.right = self.pantalla_rect.right
        self.rectder.top = self.pantalla_rect.top


    def blitme(self):
        self.pantalla.blit(self.pared_ancha_1, self.rect)
        self.pantalla.blit(self.pared_ancha_2, self.rects)
        self.pantalla.blit(self.pared_alta_izq, self.rectizq)
        self.pantalla.blit(self.pared_alta_der, self.rectder)