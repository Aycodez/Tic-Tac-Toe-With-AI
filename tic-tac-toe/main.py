from tic_tac_toe import TicTacToe
from easyAI import Negamax, AI_Player, Human_Player



def main():
    AI = Negamax(7)
    app = TicTacToe([Human_Player(), AI_Player(AI)])
    app.play()


if __name__ == '__main__':
    main()
