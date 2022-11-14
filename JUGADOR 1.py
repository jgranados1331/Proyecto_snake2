import pygame
from pygame.sprite import Sprite

#### COLOCAR EN CONFIGURACIONES EL SELF PARA EL FACTOR VELOCIDAD DE LA SERPIENTE
### self.factor_velocidad_serpiente = 1.5
###



class serpiente_1(Sprite):
    """Comportamiento de la primera serpiente"""

    def __init__(self, ai_configuraciones, pantalla):
        """Inicia la serpiente y la posicion de partida"""
        super(serpiente_1, self).__init__()
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Imagen de la serpiente
        color_serpiente = (0, 0, 255)
        self.image = pygame.draw.rect(pantalla, color_serpiente, [200, 150, 10, 10])
        self.pantalla_rect = pantalla.get_rect()

        # Posicion de la primera serpiente
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.center = self.pantalla_rect.center

        # Almacena un valor decimal para el centro de la nave
        self.center = float(self.rect.centerx)

        # Banderas de movimiento
        self.moving_top = False
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
    

    def update(self):
        """Actualiza la posicion de la nave segun las banderas de movimiento"""
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.ai_configuraciones.factor_velocidad_serpiente

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_configuraciones.factor_velocidad_serpiente
        
        if self.moving_top and self.rect.left < self.pantalla_rect.top:
            self.center += self.ai_configuraciones.factor_velocidad_serpiente

        if self.moving_down and self.rect.down > 0:
            self.center -= self.ai_configuraciones.factor_velocidad_serpiente

        self.rect.centerx = self.center

    
    def blitme(self):
        """Dibujar la serpiente en la ubicacion actual"""
        self.pantalla.blit(self.imagem self.rect)
    
    