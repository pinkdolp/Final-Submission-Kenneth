import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    #Paddle Class
    
    def __init__(self, color, width, height):
        # Calling the Parent Class
        super().__init__()
        
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Drawing the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        
        self.rect = self.image.get_rect()
    #Below are the paddle parameters    
    def moveUp(self, pixels):
        self.rect.y -= pixels
        
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        
        if self.rect.y > 400:
          self.rect.y = 400