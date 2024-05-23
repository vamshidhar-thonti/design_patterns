import time
from ui import GameUI
from game_logic import GamePublisher
from constants import UI_CONSTANTS

def main():
    game_ui = GameUI(
        UI_CONSTANTS.SCREEN_WIDTH.value,
        UI_CONSTANTS.SCREEN_HEIGHT.value,
        UI_CONSTANTS.ROW_COUNT.value,
        UI_CONSTANTS.COLUMN_COUNT.value
    )

    game_publisher = GamePublisher()
    initial_game_state = game_publisher.grid.get_game_state()
    game_ui.display(initial_game_state)

    game_publisher.attach(game_ui)

    running = True
    while running:
        time.sleep(0.03)
        game_publisher.run_game_logic()

if __name__ == "__main__":
    main()