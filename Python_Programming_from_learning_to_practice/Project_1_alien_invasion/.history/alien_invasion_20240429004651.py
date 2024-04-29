import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类
    """
    
    def __init__(self) -> None:
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
        # 设置背景色
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event
    
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()