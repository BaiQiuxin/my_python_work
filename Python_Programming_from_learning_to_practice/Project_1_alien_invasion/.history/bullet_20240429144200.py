import pygame
from pygame.sprite import _Group, Sprite

class Bullet(Sprite):
    """管理飞船所有子弹的类"""
    
    def __init__(self, ai_game) -> None:
        """在飞船的当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_gamex.symmetric_difference(y)