
from player import Player
from board import Board
from typing import List, Tuple

def main():
    print('Tic-Tac')

    board: Board = Board(4)
    p: Tuple[Player, Player] = Player('o'), Player('x')
    current_player: int = 0
    current_move: int = None
    status: int = -1

    while status == -1:
        print(f'{str(p[current_player])} turn:')
        print(str(board))
        current_move = p[current_player].move(board)
        board.update(current_move, current_player)

        status = board.finished()
        current_player = 0 if current_player == 1 else 1

    print(str(board))
    if status == 2:
        print('Game ended in draw!')
    else:
        print(f'Game ended! Player {p[status]} is victorious!')

if __name__ == '__main__':
    main()