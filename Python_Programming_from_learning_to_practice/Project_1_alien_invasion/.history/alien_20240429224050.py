import pygame
from pygame.sprite import _Group, Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_game) -> None:
        """初始化外星人并设置其初始位置"""
        super().__init__()
        