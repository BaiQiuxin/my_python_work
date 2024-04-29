import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_game) -> None:
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储每个外星人的精确水平位置
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        
    
    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
