import sys

import pygame


def events_verify(ai_configuraciones,pantalla):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def screen_update(ai_configuraciones, pantalla):
    pantalla.blit(ai_configuraciones.background_game,(0,0))
    pantalla.blit(ai_configuraciones.first,(25,50))
    pygame.display.flip()