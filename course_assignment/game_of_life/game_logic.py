import random
from typing import List
from abc import ABC, abstractmethod

from constants import UI_CONSTANTS
from ui import GameUI

class GridState(ABC):
    def __init__(self) -> None:
        self.game_state = None
        
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def get_game_state(self):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def notify(self):
        pass

class InitialGridState(GridState):
    def __init__(self) -> None:
        super().__init__()
        self.game_state = [
            [
                0 if random.randint(0, 9) < 8 else 1 for _ in range(UI_CONSTANTS.COLUMN_COUNT.value)
            ] for _ in range(UI_CONSTANTS.ROW_COUNT.value)
        ]

    def next(self, grid: 'Grid'):
        game_state = grid.get_game_state()
        grid.grid_state = NextGridState(game_state)
        grid.grid_state.next(grid)

    def get_game_state(self):
        return self.game_state
    
class NextGridState(GridState):
    def __init__(self, game_state) -> None:
        self.game_state = game_state

    def get_adjacent_cells(self, cell):
        adjacent_cells = []
        x, y = cell
        surrounding_cells_x = [x-1, x, x+1]
        surrounding_cells_y = [y-1, y, y+1]

        for x_value in surrounding_cells_x:
            for y_value in surrounding_cells_y:
                if x_value < 0 or y_value < 0 \
                    or x_value > UI_CONSTANTS.ROW_COUNT.value - 1 \
                    or y_value > UI_CONSTANTS.COLUMN_COUNT.value - 1 \
                    or (x_value, y_value) == (x, y):
                    continue
                else:
                    adjacent_cells.append(self.game_state[x_value][y_value])

        return adjacent_cells

    def game_logic(self):
        game_state_copy = [row[:] for row in self.get_game_state()]
        for x_index, x in enumerate(self.get_game_state()):
            for y_index, current_cell in enumerate(x):
                adjacent_cells = self.get_adjacent_cells((x_index, y_index))
                if current_cell == 1 and adjacent_cells.count(1) in [2, 3]:
                    game_state_copy[x_index][y_index] = 1
                elif current_cell == 0 and adjacent_cells.count(1) == 3:
                    game_state_copy[x_index][y_index] = 1
                else:
                    game_state_copy[x_index][y_index] = 0

        self.game_state = game_state_copy

    def next(self, grid: 'Grid'):
        self.game_logic()
        # grid.grid_state = NextGridState(self.get_game_state())
    
    def get_game_state(self) -> list:
        return self.game_state
    
class Grid:
    grid_state: GridState = InitialGridState()

    def next(self):
        self.grid_state.next(self)

    def get_game_state(self):
        return self.grid_state.get_game_state()

class GamePublisher(Subject):

    def __init__(self) -> None:
        self._observers: List[GameUI] = []
        self.grid = Grid()

    def attach(self, observer: GameUI):
        self._observers.append(observer)

    def detach(self, observer: GameUI):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def run_game_logic(self):
        self.grid.next()
        self.notify()