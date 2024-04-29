import pygame
from pygame.sprite import _Group, Sprite

class Bullet(Sprite):
    """管理飞船所有子弹的类"""
    
    def __init__(self, ai_game) -> None:
        """在飞船的当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings =ai_game.settings
        self.color = self.settings.bullet_color
        
        # 在(0, 0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bulleet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # 用浮点数