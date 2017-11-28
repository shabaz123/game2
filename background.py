

import sys
import pygame

class Background(pygame.sprite.Sprite):
  def __init__(self, fname, loc):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.image.load(fname)
    self.rect=self.image.get_rect()
    self.rect.left, self.rect.top = loc



