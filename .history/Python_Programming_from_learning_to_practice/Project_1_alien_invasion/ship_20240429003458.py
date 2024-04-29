import pygame

class Ship:
    """管理飞船的类"""
    
    def __init__(self, ai_game) -> None:
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get