import sys
import time
import pygame
from configuraciones import Configuraciones
# COLOCAR PUNTAJE MAYOR DE QUÉ JUGADOR HACER MÁS PUNTAJE


def events_verify(ai_configuraciones,pantalla):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def screen_update(ai_configuraciones, pantalla, comida, pared_ancha_1, pared_ancha_2, pared_alta_izq, pared_alta_der):
    pantalla.blit(ai_configuraciones.background_game,(0,0))
    comida.blitme()
    pared_ancha_1.blitme()
    pared_ancha_2.blitme()
    pared_alta_izq.blitme()
    pared_alta_der.blitme()
    pygame.display.flip()


def game_over():
    """Función de fin del juego"""
    ai_configuraciones = Configuraciones()
    # Fuente para el texto de "Game Over"
    my_font = pygame.font.SysFont('times new roma', 50)

    # COMPLETAR LO DE LA VARIABLE PUNTAJE
    game_over_surfarce = my_font.render("El jugador ganador es:", False, True, pygame.Color(255, 0, 0))

    # CREAR UN OBJETO RECTANGULAR PARA EL TEXTO
    game_over_rect = game_over_surfarce.get_rect()

    # CUADRAR LA POSICIÓN DEL TEXTO
    game_over_rect.midtop = (600, 200)

    # PARA DIBUJAR EN LA PANTALLA
    ai_configuraciones.game_window.blit(game_over_surfarce, game_over_rect)
    pygame.display.flip()

    # DESPUÉS DE 5 SEGUNDOS EL PROGRAMA SE CIERRA
    time.sleep(5)

    # DESACTIVA LA LIBRERIA PYGAME
    pygame.quit()

    #QUITA EL PROGRAMA
    quit()

