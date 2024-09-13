import pygame.font

class Scoreboard:
    """显示得分信息的类"""
    
    def __init__(self, ai_game):
        """初始化显示得分设计的属性"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats