from enum import Enum

class UI_CONSTANTS(Enum):
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    # Maintain the ratio of screen width to height to make sure all cells are occupied
    ROW_COUNT:int = 80
    COLUMN_COUNT:int = 60

class COLORS(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    GREEN = (0, 255, 0)