'''
Pseudo smart rock paper scissor game
Desc: A simple rock-paper-scissor game that remembers how you play
Author: Jesper Glas
'''

from random import randint
from typing import Tuple
ALTERNATIVES: Tuple[str, str, str] = ('Rock', 'Paper', 'Scissor')
RESULTS: Tuple[str, str, str] = ('Player', 'Computer', 'Draw')

def main():
    print('Rock Paper Scissor')

    loop()

def loop():
    print(f'The computer has choosen, what do you play?')

    result: Tuple[int, int] = player_turn(), computer_turn()
    print(f'Player plays {ALTERNATIVES[result[0]]}\nComputer plays: {ALTERNATIVES[result[1]]}')
    
    winner: int = determine_winner(result)
    print_result(winner)

def player_turn() -> int:
    valid: bool = False
    while not valid:
        try:
            player: int = int(input(f'[0] {ALTERNATIVES[0]}\n[1] {ALTERNATIVES[1]}\n[2] {ALTERNATIVES[2]}\n>'))

            if player in range(3):
                valid = True
            else:
                raise ValueError
                
        except ValueError:
            print('Please enter a valid number corresponding to the alternatives!')
    
    return player

def computer_turn() -> int:
    computer: int = randint(0, 2)

    return computer

def determine_winner(res: Tuple[int, int]) -> int:
    if res[0] == res[1]:
        return 2
    else:
        if res[0] == 0:
            return 0 if res[1] == 2 else 1
        elif res[0] == 1:
            return 0 if res[1] == 0 else 1
        elif res[0] == 2:
            return 0 if res[1] == 1 else 1

def print_result(winner: int) -> None:
    if winner == 0:
        print('Player wins!')
    elif winner == 1:
        print('Computer wins!')
    else:
        print('It is a draw!')

if __name__ == '__main__':
    main()