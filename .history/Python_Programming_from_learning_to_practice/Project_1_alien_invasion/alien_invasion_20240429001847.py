import sys

import pygame

class AlienInvasion:
    """管理游戏资源和行为的类
    """
    
    def __init__(self) -> None:
        """初始化游戏并创建游戏资源"""
        pygame.init()
        