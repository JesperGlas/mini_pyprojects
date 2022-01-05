'''
Madlib Gen
Desc: A madlib generator.
Author: Jesper Glas
'''

from typing import List

PATH: str = 'in.txt'    # Path to the input file

def main():
    print(f'Madlib generator!')
    
    raw_data = load_file(PATH)  # Load the file to a string
    parsed_data = parse_file(raw_data) # Parse the file to a list with spaces to fill as separate elements
    res = complete(parsed_data)   # Ask for user input and update madlib
    print(res)


def load_file(path: str) -> str:
    with open(path, 'r') as f:
        data: str = ''.join([line for line in f.readlines()])

    return data

def parse_file(data: str) -> List[str]:
    data: List[str] = data.split('*')

    return data

def complete(data: List[str]) -> str:
    res: str = ''
    for elem in data:
        if 'verb' in elem or 'adjective' in elem or 'noun' in elem:
            res += str(input(f'Please enter a {elem.capitalize()}: '))
        else:
            res += elem

    return res

if __name__ == '__main__':
    main()