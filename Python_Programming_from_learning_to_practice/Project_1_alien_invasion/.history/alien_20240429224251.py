import pygame
from pygame.sprite import _Group, Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_game) -> None:
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        
        #加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #每个外星人最初都在屏幕的左上角附近
        self.rect.x = 