'''
Testing suite for sorting algorithms
Author: Jesper Glas
'''
import logging
import time
from random import randint
from typing import List

logging.basicConfig(filename="sorting_algorithms.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.INFO)

N = 1000
RANDARR = list(map(lambda x: randint(0, 1000), range(0, N)))

def main():
    '''
    Function to run and compare different sorting algorithms.
    '''
    print(f'Unsorted: {RANDARR}')
    print(f'Sorted: {insertion_sort(RANDARR)}')

def insertion_sort(arr: List[int], reversed: bool = False) -> List[int]:
    '''
    Function that sorts a list of integers and returns the sorted array.

    Params:
    arr -- the original array to be sorted

    Return:
    The sorted array
    '''
    
    start = time.time_ns()
    count: int = 0
    res = []

    for x in arr:
        i: int = 0
        if len(res) == 0:
            res += [x]
        elif x <= res[0]:
            res = [x] + res
        elif x >= res[len(res)-1]:
            res = res + [x]
        else:
            while x > res[i]: i +=1
            head = res[:i]
            tail = res[i:]
            res = head + [x] + tail
        count += 1 + i

    end = time.time_ns()
    elapsed = end - start

    log('Linear Sort', N, elapsed, count)

    return res

def log(name: str, n: int, time, op: int):
    output = f"""
    {name} results:
    List has {n} elements
    Time: {time}
    Operations: {op}
    """
    logger.info(output)

if __name__ == '__main__':
    main()