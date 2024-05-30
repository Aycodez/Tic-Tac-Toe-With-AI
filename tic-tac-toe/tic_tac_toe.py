import pygame
from pygame.locals import *
from itertools import product
from easyAI import TwoPlayersGame


class TicTacToe(TwoPlayersGame):
    def __init__(self, players):
        global screen, again_rect, font
        pygame.init()
        self.players = players
        self.clicked = False
        self.nplayer = 1
        self.screen_height = self.screen_width = 300
        self.line_width = 6
        self.colors = (255, 0, 0), (0, 255, 0), (0, 0, 255)
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Tic Tac Toe')

        font = pygame.font.SysFont(None, 40)

        # set up a rectangle for "Play Again" Option
        again_rect = Rect(self.screen_width // 2 - 80, self.screen_height // 2, 160, 50)

        # # create empty 3 x 3 list to represent the grid
        self.board = [0] * 9

        # changing the position into integers that can be used as index in the list
        self.switch = {(j[1], j[0]): i for i, j in enumerate(product([0, 1, 2], repeat=2))}

    def possible_moves(self):
        return [a + 1 for a, b in enumerate(self.board) if b == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    def loss_condition(self):
        possible_combinations = [[1, 4, 7], [2, 5, 8], [3, 6, 9],
                                 [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]

        return any([all([(self.board[i - 1] == self.nplayer)
                         for i in combination]) for combination in possible_combinations])

    # Check if the game is over
    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    # Compute the score
    def scoring(self):
        return -100 if self.loss_condition() else 0

    def restart(self):
        self.board = [0] * 9
        self.clicked = False
        self.nplayer = 2

    def draw_board(self):
        bg = (255, 255, 210)
        grid = (100, 100, 100)
        screen.fill(bg)
        for x in range(1, 3):
            pygame.draw.line(screen, grid, (0, 100 * x), (self.screen_width, 100 * x), self.line_width)
            pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, self.screen_height), self.line_width)

    def draw_markers(self):
        x_pos = 0
        index = 0

        for _ in range(3):
            y_pos = 0
            for _ in range(3):

                if self.board[index] == 1:
                    pygame.draw.line(screen, self.colors[0], (x_pos * 100 + 15, y_pos * 100 + 15),
                                     (x_pos * 100 + 85, y_pos * 100 + 85), self.line_width)
                    pygame.draw.line(screen, self.colors[0], (x_pos * 100 + 85, y_pos * 100 + 15),
                                     (x_pos * 100 + 15, y_pos * 100 + 85), self.line_width)
                if self.board[index] == 2:
                    pygame.draw.circle(screen, self.colors[1], (x_pos * 100 + 50, y_pos * 100 + 50), 38,
                                       self.line_width)
                y_pos += 1
                index += 1
            x_pos += 1

    def draw_game_over(self, winner):
        if self.possible_moves() == [] and not self.loss_condition():
            end_text = "Tie!"
        else:
            end_text = str(winner) + " wins!"

        end_img = font.render(end_text, True, self.colors[-1])
        pygame.draw.rect(screen, self.colors[1],
                         (self.screen_width // 2 - 100, self.screen_height // 2 - 60, 200, 50))
        screen.blit(end_img, (self.screen_width // 2 - 100, self.screen_height // 2 - 50))

        again_text = 'Play Again?'
        again_img = font.render(again_text, True, self.colors[-1])
        pygame.draw.rect(screen, self.colors[1], again_rect)
        screen.blit(again_img, (self.screen_width // 2 - 80, self.screen_height // 2 + 10))

    def play_again(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise Exception

            if event.type == pygame.MOUSEBUTTONDOWN and not self.clicked:
                self.clicked = True
            if event.type == pygame.MOUSEBUTTONUP and self.clicked:
                self.clicked = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    self.restart()

