class Settings():
    """store all settings in this game"""

    def __init__(self, bg_color=''):
        """initialize game's setting"""
        self.screen_width = 1200
        self.screen_height = 800
        if bg_color == 'skyblue':
            self.bg_color = (0, 255, 255)
        elif bg_color == 'gray':
            self.bg_color = (128, 128, 128)
        else:
            self.bg_color = (230, 230, 230)

    
