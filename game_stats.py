class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.stars_pass = 0
       
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.stars_pass =0