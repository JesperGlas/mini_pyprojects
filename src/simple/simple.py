'''
Simple Problems
Desc: Various simple problems solved with single functions
Author: Jesper Glas
'''

from typing import Dict, List, Tuple

def main():
    print('Testing..')
    balanced_para(2)

def first_recurring(seq: str) -> str:
    '''
    First Recurring:
        DESC: Returns the first recurring element in a string

        PARAMS:
            seq: str    - The string to be examined
        
        RETURN:
            str         - The first recurring element in the string, None if there are no recurring elements.
    '''
    H: Dict[str, int] = {}  # History of occurences of each char in the sequence
    for char in seq:
        # Go through each character in the sequence
        if char in H.keys():
            # Return the character if it's already in the history dictionary
            return char
        # If not, add it's occurence
        H[char] = 1
    # If no occurences are found, return None
    return None

def anagram(s1: str, s2: str) -> bool:
    '''
    Anagrams:
        DESC: Determines if two strings are anagrams of each other. If the ones letters can be used to spell the other one.

        PARAMS:
            s1: str - The first string
            s2: str - The second string

        RETURN:
            bool    - True if the two strings are anagrams of each other, False otherwise. 
    '''
    if len(s1) != len(s2):
        # Check if the length are the same, otherwise return False.
        return False
    # If they are anagrams the sorted list of letters will be the same
    return sorted(s1) == sorted(s2)

def first_and_last(arr: List[int], target: int) -> Tuple[int, int]:
    '''
    First and Last:
        DESC: Finds the first and last index of a target int in an array.

        PARAMS:
            arr: List[int]  - The array of integers
            target: int     - The target int

        RETURN:
            Tuple[int, int] - (First, Last) index of the target in the arr, (-1, -1) if the target isn't in the arr.
    '''
    first: int = -1
    last: int = -1
    if target in arr:
        first = arr.index(target)  # Finds first occurence
        arr.reverse()
        last = len(arr) - arr.index(target) -1  # Finds last occurence

    return first, last

def kth_largest(arr: List[int], k: int, unique: bool=False) -> int:
    '''
    K:th Largest:
        DESC: Finds the k:th largest element in an array of integers.

        PARAMS:
            arr: List[int]  - An array of integers
            k: int          - k:th largest element to return
            unique: bool    - Determines if the arr should be a set of unique elements or all elements (Default: False)
        
        RETURN:
            int             - The k:th largest element in the arr. Returns the last element in arr if k is longer than array.
    '''
    index: int = k-1    # Compensate for index starting at 0
    unique: List[int] = sorted(set(arr), reverse=True) if unique else sorted(arr, reverse=True)

    return unique[index] if len(unique) > index else unique[len(unique)-1]

def balanced_para(n: int) -> List[str]:
    '''
    Balanced Parentheses:
        DESC: Generates all balanced combinations of n pair of parentheses.

        PARAMS:
            n: int  - Pairs of parentheses

        RETURN:
            List[str]   - All unique combinations of balanced parentheses
    '''
    combs: List[List[str]] = [] # List of valid combinations
    balanced_para_rec(2*n, 0, [], combs)    # Recursive function.
    return combs
    

def balanced_para_rec(depth: int, balance: int, current: List[str], combinations: List[List[str]]) -> None:
    '''
    Balanced Parentheses Recursive:
        DESC: The recursive function that finds all valid combinations of balanced parentheses.

        PARAMS:
            depth: int                      - Current depth of reccursion (Max n*2)
            balance: int                    - Balance (Difference between '(' and ')' in current combination)
            current: List[str]              - Current combination state
            combinations: List[List[str]]   - List of valid combinations

    '''
    if balance < 0 or balance > depth:
        # balance < 0 makes sure that we always begins with an opening parentheses
        # balance > depth makes sure that it's possible to close the combination before reaching end of reccursion
        # If any of these to are True we have an invalid combination and therefore returns
        return
    elif depth == 0 and balance == 0:
        # If we reach depth=0 with a balance=0 we have a valid combination which we add to our result
        combinations.append(''.join(current))
    else:
        # Recursive step add opening parenthese '('
        current.append('(')
        balanced_para_rec(depth-1, balance+1, current, combinations)
        current.pop()
        # Recursive step add closing parenthese ')'
        current.append(')')
        balanced_para_rec(depth-1, balance-1, current, combinations)
        current.pop()

if __name__ == '__main__':
    main()