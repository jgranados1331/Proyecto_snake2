import pygame
import game_functions as gf
from configuraciones import Configuraciones
from comida import Comida
from paredes import pared
def run_game():
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption((ai_configuraciones.name_game))
    pygame.display.set_icon((ai_configuraciones.icon))

    comida = Comida(ai_configuraciones,pantalla)
    comida2 = Comida(ai_configuraciones,pantalla)
    pared_ancha_1 = pared(ai_configuraciones, pantalla)
    pared_ancha_2 = pared(ai_configuraciones, pantalla)
    pared_alta_izq= pared(ai_configuraciones, pantalla)
    pared_alta_der= pared(ai_configuraciones, pantalla)
    

    while True:
        gf.screen_update(ai_configuraciones,pantalla,comida,comida2,pared_ancha_1, pared_ancha_2,pared_alta_izq,pared_alta_der)
        gf.events_verify(ai_configuraciones,pantalla)

run_game()