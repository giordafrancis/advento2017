"""
https://adventofcode.com/2017/day/2
"""
from typing import List
import itertools

TEST_INPUT = """5 1 9 5
7 5 3
2 4 6 8"""


def process_row(string: str)-> List[int]:
    return [int(x) for x in string.split()]

def row_checksum(row: List[int])-> int:
    """
    Return the subtraction of the maximum and minimum value
    per row
    """
    return max(row) - min(row) 

def spreadsheet_checksum(string: str) -> int:
    """
    For each row calculate the row_checksum
    and sum all the values
    """
    rows = [process_row(row) for row in string.split('\n') if row]
    return sum(row_checksum(row) for row in rows)

assert spreadsheet_checksum(TEST_INPUT) == 18

TEST_INPUT2 = """5 9 2 8
9 4 7 3
3 8 6 5"""

def row_even_div(row: List[int])-> int:
    """ For each row that are exactly 2 values
    that are divisible, return the quotient
    """
    row_permutations = itertools.permutations(row, 2)
    even_div = [x // y for x, y in row_permutations if x % y == 0]
    assert len(even_div) == 1
    return even_div[0]

def spreadsheet_evendiv(string: str) -> int:
    rows = [process_row(row) for row in string.split('\n') if row]
    return sum(row_even_div(row) for row in rows)
            
assert row_even_div([5, 9, 2, 8]) == 4
assert row_even_div([9, 4, 7, 3]) == 3
assert row_even_div([3, 8, 6, 5]) == 2
assert spreadsheet_evendiv(TEST_INPUT2) == 9

if __name__ == "__main__":
    with open("day02_input.txt", 'r') as file:
        INPUT = file.read()
        print(spreadsheet_checksum(INPUT))
        print(spreadsheet_evendiv(INPUT))