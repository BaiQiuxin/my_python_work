import pygame
from pygame.sprite import _Group, Sprite

class Bullet(Sprite):
    """管理飞船所有子弹的类"""
    
    def __init__(self, *groups: AbstractGroup[_SpriteSupportsGroup]) -> None:
        super().__init__(*groups)