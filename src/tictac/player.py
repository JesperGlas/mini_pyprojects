from typing import List
from board import Board
from random import randint

class Player:
    def __init__(self, id: str):
        self.id: str = id

    def move(self, board: Board) -> int:
        valid_move = False
        pos: int = -1

        while not valid_move:
            try:
                pos = int(input(f'Place a mark in an empty tile [1-{len(board.get())}]')) -1 # -1 to compensate for index starting at 1
                if pos not in range(0, len(board.get())):
                    raise ValueError('That is not a valid tile..')
                elif board.at_pos(pos) != -1:
                    raise ValueError('That tile is already occupied..')
                else:
                    valid_move = True
            except ValueError as e:
                print(e)
                print('Try again..')
        
        return pos

    def __str__(self) -> str:
        return f'Player {self.id}'

class ComputerPlayer(Player):
    def __init__(self, id: str):
        return super().__init__(id)

    def move(self, board: Board) -> int:
        valid_move: bool = False
        pos: int = -1
        
        while not valid_move:
            pos = randint(0, len(board.get())-1)
            if board.at_pos(pos) == -1:
                valid_move = True
        
        return pos