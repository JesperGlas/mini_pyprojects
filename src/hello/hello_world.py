#!/usr/bin/env python
"""
Hello
Desc: A simple project with one function that greets you by your name. Used to set up documentation and testing.
Author: Jesper Glas
"""
import sys
from typing import List

def hello(names: List[str] = ["you"]) -> str:
    """
    A simple function that greets you by your name.

    Params:
    name -- the name to be greeted, default "you"
    """

    names = ", ".join(names)

    return f'Hello {names}!'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        names: List[str] = list(filter(lambda name: isinstance(name, str), sys.argv[1:]))
    else:
        names = ["you"]
    
    print(hello(names))