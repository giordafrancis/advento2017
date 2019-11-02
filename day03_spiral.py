"""
https://adventofcode.com/2017/day/3
"""

# I've had to checked Joel Grus implementation as I was stuck in part 1 and part 2

from typing import Tuple, List, Iterator
from collections import defaultdict
import math
import itertools

def corner_odd_square(num: int)-> int:
    """"
    Within a spiral range -> from corner to last before corner, eg. 25 to 48 
    all numbers have the same corner_odd_square
    Finds the corner odd square number of a given number 
    """
    sqrt_num = int(math.sqrt(num))

    if sqrt_num % 2 == 0:
        return sqrt_num - 1
    else:
        return sqrt_num

assert corner_odd_square(1) == 1
assert corner_odd_square(9) == 3
assert corner_odd_square(25) == 5
assert corner_odd_square(80) == 7
assert corner_odd_square(26) == 5
assert corner_odd_square(48) == 5
assert corner_odd_square(49) == 7

def find_coordinates(num: int) -> Tuple[int, int]:
    """
    Returns the coordinates of num within the spiral
    defaults to (0,0) if negative num is provided.
    """
    # num has to be positive
    num = max((num, 1))

    sqrt_num = corner_odd_square(num)
    square = sqrt_num ** 2

    # calculate the num corner (x, y)
    x = y = sqrt_num // 2

    side_len = sqrt_num + 1
   
    # if num is the corner num
    if square == num:
        return x, y
    # if num is on 1st vertical section after corner
    elif num <= side_len + square:
        excess = num - square 
        return (x + 1, y - excess + 1)
    # if num is on 1st horizontal section
    elif num <= 2 * side_len + square:
        excess = num - square - side_len
        return (x + 1 - excess, y - side_len + 1)
    # if num  is on 2nd vertical section
    elif num <= 3 * side_len + square:
        excess = num - square - 3 * side_len
        return (x - side_len + 1, y + 1 + excess)
    # num is on last section leading to next corner
    else:
        excess = num - square - 4 * side_len
        return (x + 1 + excess, y + 1)

assert find_coordinates(25) == (2, 2)
assert find_coordinates(9) == (1, 1)
assert find_coordinates(1) == (0, 0)
assert find_coordinates(26) == (3, 2)
assert find_coordinates(31) == (3, -3)
assert find_coordinates(32) == (2, -3)
assert find_coordinates(33) == (1, -3)
assert find_coordinates(37) == (-3, -3)
assert find_coordinates(38) == (-3, -2)
assert find_coordinates(39) == (-3, -1)
assert find_coordinates(40) == (-3, 0)
assert find_coordinates(46) == (0, 3)
assert find_coordinates(45) == (-1, 3)
assert find_coordinates(44) == (-2, 3)
assert find_coordinates(48) == (2, 3)

def manhattan_dis(coordinates: Tuple[int, int]) -> int:
    """
    Calculates the Manhattan Distance to origin (0, 0)
    """
    x, y = coordinates
    return abs(x) + abs(y)

assert manhattan_dis((0,0)) == 0
assert manhattan_dis((0,-10)) == 10

assert(manhattan_dis(find_coordinates(1024))) == 31
assert(manhattan_dis(find_coordinates(23))) == 2

# work on the type checking below
def get_adjacent_squares(loc: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    """
    Give a location generates the adjacent squares locoations
    """
    x, y = loc

    adjacent = [(x - 1, y), (x + 1, y), (x , y -1), (x, y + 1), 
                (x - 1, y - 1), (x + 1, y + 1), 
                (x - 1, y + 1), (x + 1, y - 1) ]
    for square in adjacent:
        yield square

def first_value_written_larger(num:int) -> int:
    """
    Returns first value written larger then num
    """
    values = defaultdict(int)
    values[(0,0)] = 1
    
    for count in itertools.count(2):
        loc = find_coordinates(count)
        sum_adjacent = sum(values[loc] for loc in get_adjacent_squares(loc))
        values[loc] = sum_adjacent 
        if sum_adjacent > num:
            break
    return sum_adjacent

assert first_value_written_larger(2) == 4
assert first_value_written_larger(11) == 23
assert first_value_written_larger(747) == 806


PUZZLE_INPUT = 265149

if __name__ == "__main__":
    coordinates = find_coordinates(PUZZLE_INPUT)
    print(manhattan_dis(coordinates)) 
    print(first_value_written_larger(PUZZLE_INPUT))












