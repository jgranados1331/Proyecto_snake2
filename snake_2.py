import pygame
import game_functions as gf
from configuraciones import Configuraciones

def run_game():
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption((ai_configuraciones.name_game))
    pygame.display.set_icon((ai_configuraciones.icon))
    

    while True:
        gf.screen_update(ai_configuraciones,pantalla)
        gf.events_verify(ai_configuraciones,pantalla)

run_game()