import pygame.font

class Scoreboard:
    """显示得分信息的类"""
    
    def __init__(self, ai_game):
        """初始化显示得分设计的属性"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        