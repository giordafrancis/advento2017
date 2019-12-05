"""
https://adventofcode.com/2017/day/10
"""
from typing import List

def hash(lengths:List[int], inputs:List[int]=list(range(256))) -> int:

    inputs = inputs[:]
    skip_size = 0
    loc_start = 0
    L = len(inputs)
    print(inputs)
    for l in lengths:
        loc_end = (loc_start + l ) % L
        
        print("start", loc_start)
        print("end", loc_end)
        print("lenght", l)
        print("skip_size", skip_size)
               
        if l == 0:
            pass
        elif loc_end > loc_start: # no wrap around
            inputs[loc_start: loc_end] = inputs[loc_start:loc_end][::-1]
        else: #loc_end <= loc_start with wrap around 
            reverse = (inputs[loc_start:] + inputs[:loc_end])[::-1]
            inputs[loc_start:] = reverse[:(L - loc_start)]
            inputs[:loc_end] = reverse[(L - loc_start):]
        
        loc_start = (loc_start + l + skip_size) % L
        skip_size += 1
        print(inputs)
    return inputs[0] * inputs[1]

TEST_LENS = [3, 4, 1, 5]
assert hash(lengths = TEST_LENS, inputs=list(range(5))) == 12

PART_1 = [63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24]

print(hash(lengths=PART_1))