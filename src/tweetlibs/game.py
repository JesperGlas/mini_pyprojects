'''
Tweetlibs
Desc: A madlib generator with tweets.
Author: Jesper Glas
'''

from os import register_at_fork
from typing import List, Dict
import random as rd
import re

PATH: str = 'trump.txt'    # Path to the input file
TRANSLATE: Dict[str, str] = {
    '@': 'Mention',
    '#': 'Hashtag',
    '-': 'Name',
    'https': 'Website'
}

def main():
    print(f'Madlib generator!')
    
    tweets = load_file(PATH)  # Load the file to a string
    tweet: str = rd.choice(tweets)
    parsed_tweet: List[str] = parse_tweet(tweet)
    res: str = complete(parsed_tweet)
    print(res)


def load_file(path: str) -> str:
    with open(path, 'r') as f:
        tweets: List[str] = [line for line in f.readlines()]

    return tweets

def parse_tweet(data: str) -> List[str]:
    res: List[str] = []
    data: List[str] = data.split(' ')
    for word in data:
        word = word.strip()
        word = re.sub('["]', '', word)
        res.append(translate(word))

    return res

def translate(raw: str) -> str:
    if len(raw) > 0:
        if raw[0] == '@':
            return '@'
        elif raw[0] == '#':
            return '#'
        elif raw[0] == '-':
            return '-'
        else:
            return raw
    return raw

def complete(data: List[str]) -> str:
    res: str = ''
    for elem in data:
        if elem in TRANSLATE.keys():
            res += str(input(f'Please enter a {elem}{TRANSLATE[elem].capitalize()}: '))
        else:
            res += elem
        res += ' '

    return res

if __name__ == '__main__':
    main()