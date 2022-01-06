from typing import List
from board import Board

class Player:
    def __init__(self, id: str):
        self.id: str = id

    def move(self, board: Board) -> int:
        valid_move = False
        move: int = -1

        while not valid_move:
            try:
                move = int(input(f'Place a mark in an empty tile [1-{len(board.get())}]')) -1 # -1 to compensate for index starting at 1
                if move not in range(0, len(board.get())):
                    raise ValueError('That is not a valid tile..')
                elif board.at_pos(move) != -1:
                    raise ValueError('That tile is already occupied..')
                else:
                    valid_move = True
            except ValueError as e:
                print(e)
                print('Try again..')
        
        return move

    def __str__(self) -> str:
        return f'Player {self.id}'