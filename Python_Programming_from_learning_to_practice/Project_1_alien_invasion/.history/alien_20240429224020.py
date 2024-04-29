import pygame
from pygame.sprite import _Group, Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, *groups: AbstractGroup[_SpriteSupportsGroup]) -> None:
        super().__init__(*groups)