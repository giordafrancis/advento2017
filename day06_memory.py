"""
https://adventofcode.com/2017/day/6
"""

from typing import List, Tuple
import itertools
from collections import defaultdict

mem_bank = List[int]

def redistribute(bank: mem_bank) -> mem_bank:
    """
    finds max value within bank with lowest index
    calculates memory required to redistribute
    redistributes memory and returns new bank
    """
    # make copy not to destroy list
    bank = bank[:]
    num_blocks = len(bank)
    max_val = max(bank)
    # min idx of max value of bank
    idx = min(idx for idx, block in enumerate(bank) if block == max_val)
    mem = bank[idx]
    bank[idx] = 0
    # based on example seems the correct way to redistribute
    take = mem // (num_blocks - 1)

    if not take:
        take = 1
    else:
        take 

    curr_idx = idx 
    while max_val > 0:
        if curr_idx == num_blocks - 1:
            curr_idx = 0
        else:
            curr_idx += 1
        # max val needs to be fully redistributed
        if max_val >= take:
            bank[curr_idx] += take
        else:
            bank[curr_idx] += max_val
        max_val -= take
    return bank
    
assert redistribute([0, 2, 7, 0]) == [2, 4, 1, 2]
assert redistribute([2, 4, 1, 2]) == [3, 1, 2, 3]
assert redistribute([3, 1, 2, 3]) == [0, 2, 3, 4]
assert redistribute([0, 2, 3, 4]) == [1, 3, 4, 1]
assert redistribute([1, 3, 4, 1]) == [2, 4, 1, 2]

# reviewed other implementations after 
# really over cooked it so trying again!!

def redistribute2(memory: mem_bank) -> mem_bank:
    """
    finds max value within bank with lowest index
    calculates memory required to redistribute
    redistributes memory and returns new bank
    """
    num_blocks = len(memory)
    max_val = max(memory)
    idx = min(i  for i, val in enumerate(memory) if val == max_val)
    memory[idx] = 0
    
    for _ in range(max_val):
        idx = (idx + 1) % num_blocks
        memory[idx] += 1
    return memory

assert redistribute2([0, 2, 7, 0]) == [2, 4, 1, 2]
assert redistribute2([2, 4, 1, 2]) == [3, 1, 2, 3]
assert redistribute2([3, 1, 2, 3]) == [0, 2, 3, 4]
assert redistribute2([0, 2, 3, 4]) == [1, 3, 4, 1]
assert redistribute2([1, 3, 4, 1]) == [2, 4, 1, 2]

def num_cycles(bank: mem_bank) -> int:
    """
    Given a memory bank 
    iteratively redistributes max value bank
    until same state is repeated
    returns num cycles to same state
    """
    seen = set()
    for count in itertools.count(1):
        redistribute2(bank)         # mutate in place
        bank_tuple = tuple(bank)    # list are not hashable       
        if bank_tuple in seen:      # set/dict lookups are fast
            return count 
        else:
            seen.add(bank_tuple)

def num_cycles_between(bank: mem_bank) -> int:
    """
    Given a memory bank 
    iteratively redistributes max value bank
    until same state is repeated
    returns num cycles between repeated states
    """
    seen = defaultdict(int)
    for count in itertools.count(1):
        redistribute2(bank)         # mutate in place
        bank_tuple = tuple(bank)    # list are not hashable       
        if bank_tuple in seen.keys():      # set/dict lookups are fast
            return count - seen[bank_tuple] 
        else:
            seen[bank_tuple] = count


assert num_cycles([0, 2, 7, 0]) == 5
assert num_cycles_between([0, 2, 7, 0]) == 4

if __name__ == "__main__":
    with open("day06_input.txt" ,'r') as file:
        text_inputs = file.read()
        part1_input = [int(block) for block in text_inputs.split()]
        part2_input = part1_input[:]
        print(num_cycles(part1_input))
        print(num_cycles_between(part2_input))













































