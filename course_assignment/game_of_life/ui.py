import pygame
from abc import ABC, abstractmethod

from constants import COLORS

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class GameUI(Observer):
    def __init__(self, screen_width, screen_height, rows_count, cols_count) -> None:
        pygame.init()
        self.rows_count = rows_count
        self.cols_count = cols_count
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_width = screen_width // rows_count
        self.cell_height = screen_height // cols_count
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Conway's Game of Life")

    def draw_cells(self, game_state):
        for y in range(self.cols_count):
            for x in range(self.rows_count):
                cell = pygame.Rect(
                    x * self.cell_width,
                    y * self.cell_height,
                    self.cell_width,
                    self.cell_height
                )
                if game_state[x][y] == 1:
                    pygame.draw.rect(self.screen, COLORS.BLACK.value, cell)

    def draw_grid(self):
        for y in range(0, self.screen_height, self.cell_height):
            for x in range(0, self.screen_width, self.cell_width):
                cell = pygame.Rect(x, y, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, COLORS.GRAY.value, cell, 1)

    def display(self, game_state):
        self.screen.fill(COLORS.WHITE.value)
        self.draw_grid()
        self.draw_cells(game_state)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def update(self, subject):
        game_state = subject.grid.get_game_state()
        self.display(game_state)
