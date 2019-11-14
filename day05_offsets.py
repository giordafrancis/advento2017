"""
https://adventofcode.com/2017/day/5/input
"""

from typing import List
import itertools


def num_steps(offsets: List[int]) -> int:
    """
    Based on a List of offsets.
    Returns the number of steps required to exit
    the list length. Local offset is increment by +1 
    after jump
    """
    # prevents list destruction
    offsets = offsets[:]
    out = len(offsets)
    loc = 0

    for steps in itertools.count():
        if loc >= out:
            return steps
        # find current value
        curr = offsets[loc]
        # increment current value by +1 step
        offsets[loc] = curr + 1
        # move location by current value
        loc += curr
      

assert num_steps([0, 3, 0, 1, -3]) == 5


def num_steps2(offsets: List[int]) -> int:
    """
    Based on a List of offsets.
    Returns the number of steps required to exit
    the list length. 
    Local offset is increment by +1 if smaller then 3
    otherwise decrease by -1;  after jump
    """
    # prevents list destruction
    offsets = offsets[:]
    out = len(offsets)
    loc = 0

    for steps in itertools.count():
        # prevents loc smaller then 0
        loc = max(0, loc)
        if loc >= out:
            return steps
            
        # find current offset value
        curr = offsets[loc]
        if curr < 3:
            # increment current value by +1 step
            offsets[loc] = curr + 1
        else:
            offsets[loc] = curr - 1
        
        # move location by current value
        loc += curr

assert num_steps2([0, 3, 0, 1, -3]) == 10

if __name__ == "__main__":
    with open("day05_input.txt", 'r') as file:
        inputs = file.read()
        offsets = [int(offset) for offset in inputs.split("\n") if offset]
        print(num_steps(offsets))
        print(num_steps2(offsets))

            

