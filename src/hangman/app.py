'''
Hangman
Desc: The hangman game
Author: Jesper Glas
'''

from typing import List
from random import randint

WORDS: List[str] = ['helloworld', 'python', 'syntax', 'pythonprojects']

def main():
    print('Welcome to Hangman!')
    loop('helloworld')

def loop(word: str) -> str:
    tested: List[str] = []
    done: bool = False
    state: str = '_'*len(word)
    wrong: int = 0

    while not done:
        print(f'{state}')
        print(f'Tested: {", ".join(tested)}')
        print(f'Errors: {wrong}')
        letter = user_input(tested)
        tested.append(letter)
        state = update(letter, word, state)
        wrong += 0 if correct(letter, word) else 1

        done = True if state == word else False

    print('Congratulations! You did it!')

def user_input(tested: List[str]) -> str:
    valid_input: bool = False

    while not valid_input:
        try:
            letter = str(input('Please enter the letter you wish to try:\n'))

            if letter in tested:
                raise ValueError('You have already tried that letter!')
            elif len(letter) != 1:
                raise ValueError('The input can only be one single character!')
            else:
                valid_input = True

        except ValueError as e:
            print(e)
            print('Try again:')

    return letter

def correct(letter: str, word: str) -> bool:
    return True if letter in word else False

def update(letter: str, word: str, state: str) -> str:
    new_state: List[str] = list(state)
    for i, char in enumerate(word):
        new_state[i] = letter if char == letter else state[i]
    
    return ''.join(new_state)


if __name__ == '__main__':
    main()