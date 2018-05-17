import pygame

class Collider(pygame.sprite.Sprite):

    """Sprites invisibles que son colocatos sobre algunas partes del fondo del juego
       y que pueden ser collisionados (piso, obstaculos, etc)"""

    def __init__(self, x, y, width, height, name='collider'):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height)).convert()
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
