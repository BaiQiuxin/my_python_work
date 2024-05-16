import pygame.font

class Button:
    """为游戏创建按键的类"""
    
    def __init__(self, ai_game, msg) -> None:
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        