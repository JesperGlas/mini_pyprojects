#!/usr/bin/env python
'''
Testing suite for sorting algorithms
Author: Jesper Glas
'''
import logging
import time
from random import randint
from typing import List

logging.basicConfig(filename="logs/sorting_algorithms.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.INFO)

N = 10
RANDARR = list(map(lambda x: randint(0, 1000), range(0, N)))
COUNT: int = 0

def main():
    '''
    Function to run and compare different sorting algorithms.
    '''
    print(f'Unsorted: {RANDARR}')
    print(f'Sorted: {merge_sort(RANDARR)}')


def insertion_sort(arr: List[int], reversed: bool = False) -> List[int]:
    '''
    Function that sorts a list of integers and returns the sorted list using insertion sort

    Params:
    arr -- the original list to be sorted

    Return:
    The sorted list
    '''
    res: List[int] = []

    for x in arr:
        # Check each element in list
        if len(res) == 0:
            # When sorted list is empty, add first element
            res += [x]
        elif x <= res[0]:
            # If current unsorted element is smaller than first sorted element, add at index 0
            res = [x] + res
        elif x >= res[len(res)-1]:
            # If the current unsorted element is larger than last sorted element, add at index end
            res = res + [x]
        else:
            # When current unsorted element is somewhere in the middle
            i: int = 0 # Index in sorted list
            while x > res[i]: i +=1 # Increment index while x is larger than element at index i in sorted list
            # Split sorted list at index
            head = res[:i]
            tail = res[i:]
            # Add element between head and tail
            res = head + [x] + tail

    return res

def merge_sort(arr: List[int]) -> List[int]:
    '''
    Function that sorts a list of integers using merge sort
    '''
    if len(arr) <= 1:
        # If list is shorter than two, return list
        return arr
    else:
        # Split list and call merge_sort on both halves, return merged and sorted result.
        half: int = len(arr) // 2
        l = merge_sort(arr[:half])
        r = merge_sort(arr[half:])
        return merge(l, r)
    
    
def merge(l: List[int], r: List[int]) -> List[int]:
    '''
    Function to merge and sort two lists
    '''
    res: List[int] = [] # Return array

    while len(l) > 0 and len(r) > 0:
        # While there is still elements in both input lists
        if l[0] > r[0]:
            res += [r[0]]
            r = r[1:]
        else:
            res += [l[0]]
            l = l[1:]

    while len(l) > 0:
        # While there is only elements left in the l-list
        res += [l[0]]
        l = l[1:]

    while len(r) > 0:
        # While there is only elements left in the r-list
        res += [r[0]]
        r = r[1:]

    return res

if __name__ == '__main__':
    main()