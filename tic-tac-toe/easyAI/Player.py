# import pygame
# """
# This module implements the Player (Human or AI), which is basically an
# object with an ``ask_move(game)`` method
# """
#
# # try:
# #     input = raw_input
# # except NameError:
# #     pass
#
#
# class Human_Player:
#     def __init__(self, game):
#         self.game = game
#
#     def make_move(self):
#
#         for event in pygame.event.get():
#             # handle game exit
#             if event.type == pygame.QUIT:
#                 self.game.run = False
#             # run new game
#             if not self.game.game_over:
#                 # check for mouseclick
#                 if event.type == pygame.MOUSEBUTTONDOWN and not self.game.clicked:
#                     self.game.clicked = True
#                 if event.type == pygame.MOUSEBUTTONUP and self.game.clicked:
#                     self.game.clicked = False
#                     pos = pygame.mouse.get_pos()
#                     cell_x = pos[0] // 100
#                     cell_y = pos[1] // 100
#                     # print(cell_x, cell_y)
#                     if self.game.board[self.game.switch[cell_y, cell_x]] == 0:
#                         self.move = self.game.switch[cell_y, cell_x]
#                         self.game.board[self.game.switch[cell_y, cell_x]] = self.game.player
#                         self.game.check_game_over()
#                         self.game.player *= -1
#                         print('human move: ', self.move, cell_y, cell_x)
#
#
# class AI_Player:
#     """
#     Class for an AI player. This class must be initialized with an
#     AI algorithm, like ``AI_Player( Negamax(9) )``
#     """
#
#     def __init__(self, AI_algo, name='AI'):
#         self.AI_algo = AI_algo
#         self.name = name
#         self.move = {}
#
#     def ask_move(self, game):
#         print(self.AI_algo(game))
#         return self.AI_algo(game)


import pygame
"""
This module implements the Player (Human or AI), which is basically an
object with an ``ask_move(game)`` method
"""

# try:
#     input = raw_input
# except NameError:
#     pass


class Human_Player:
    # def __init__(self):
    #     # self.game = game

    def ask_move(self,game):
        while True:
            for event in pygame.event.get():
                # handle game exit
                if event.type == pygame.QUIT:
                    raise AssertionError
                # run new game
                if not game.is_over():
                    # check for mouseclick
                    if event.type == pygame.MOUSEBUTTONDOWN and not game.clicked:
                        self.clicked = True
                    if event.type == pygame.MOUSEBUTTONUP and self.clicked:
                        self.clicked = False
                        pos = pygame.mouse.get_pos()
                        cell_x = pos[0] // 100
                        cell_y = pos[1] // 100
                        # print(cell_x, cell_y)
                        if game.board[game.switch[cell_y, cell_x]] == 0:
                            move = game.switch[cell_y, cell_x] + 1
                            # self.game.board[self.game.switch[cell_y, cell_x]] = self.game.player
                            # /game.check_game_over()
                            game.make_move(move)
                            print('my move: ', move)
                            print('board: ', game.board)

                            return move

                            # print('human move: ', self.move, cell_y, cell_x)



class AI_Player:
    """
    Class for an AI player. This class must be initialized with an
    AI algorithm, like ``AI_Player( Negamax(9) )``
    """

    def __init__(self, AI_algo, name='AI'):
        self.AI_algo = AI_algo
        self.name = name
        self.move = {}

    def ask_move(self, game):
        move = self.AI_algo(game)
        game.make_move(move)
        print('AI: ', move)
        print('board: ', game.board)

        return move
