import sys

import pygame



def events_verify(ai_configuraciones,pantalla):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def screen_update(ai_configuraciones, pantalla, comida,comida2, pared_ancha_1, pared_ancha_2, pared_alta_izq, pared_alta_der):
    pantalla.blit(ai_configuraciones.background_game,(0,0))
    comida.blitme()
    comida2.blitme()
    pared_ancha_1.blitme()
    pared_ancha_2.blitme()
    pared_alta_izq.blitme()
    pared_alta_der.blitme()
    pygame.display.flip()

