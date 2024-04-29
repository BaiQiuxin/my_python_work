class GameStats:
    """跟踪游戏的统计信息"""
    
    def __init__(self ,ai_game) -> None:
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()