from typing import Dict, List, ValuesView
import random as rd

PATH: str = 'trump.txt'

def main():
    print('Generating tweet!')
    raw_data: str = load_sentances(PATH)
    parsed_data: Dict[str, List[str]] = parse_data(raw_data)

    done: bool = False
    while not done:
        tweet: str = generate(parsed_data)
        print(tweet)
        valid_input: bool = False
        while not valid_input:
            try:
                promt: str = str(input('Enter for new tweet, q-Enter to quit [Enter/q]\n'))
                if len(promt) > 1 or promt not in ['', 'q']:
                    raise ValueError('Please enter one of the options [Enter/q]')
                elif promt == 'q':
                    done = True
                    valid_input = True
                else:
                    valid_input = True
            except ValueError as e:
                print(e)

def generate(lib: Dict[str, List[str]]) -> str:
    head: str = rd.choice(list(lib.keys()))
    next: str = rd.choice(lib[head])
    res = head

    while next != None:
        res += ' ' + next
        next = rd.choice(lib[next])

    return res.capitalize() + '.'

def load_sentances(path: str) -> List[str]:
    data: List[str] = []

    with open(path, 'r') as f:
        data = [line for line in f.readlines()]

    return ''.join(data).replace('\n', ' ').split('.')

def parse_data(raw_data: List[str]) -> Dict[str, List[str]]:
    parsed_data: Dict[str, List[str]] = {}
    for sentance in raw_data:
        parsed_data = parse_sentance(sentance.split(' '), parsed_data)

    return parsed_data

def parse_sentance(data: List[str], parsed_data: Dict[str, List[str]]) -> Dict[str, List[str]]:
    previous: str = None
    for word in data:
        if word not in parsed_data.keys():
            parsed_data[word] = []
        if previous != None and word not in parsed_data[previous]:
            parsed_data[previous].append(word)
        previous = word

    parsed_data[previous].append(None)

    return parsed_data

if __name__ == '__main__':
    main()