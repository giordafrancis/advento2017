"""
https://adventofcode.com/2017/day/1
"""

def sum_consecutive_digits(string: str)-> int:
    """
    sums matching consecutive digits from a string 
    """
    digits = [int(num) for num in string]
    
    if digits[-1] == digits[0]:
        circular = digits[0] 
    else:
        circular = 0

    return sum(num_1 for num_1, num_2 in zip(digits, digits[1:]) 
                if num_1 == num_2) + circular

assert sum_consecutive_digits("1122") == 3
assert sum_consecutive_digits("1111") == 4
assert sum_consecutive_digits("1234") == 0
assert sum_consecutive_digits("91212129") == 9


def sum_halfway_digits(string:str) -> int:
    """
    sums matching halfway digits from a string
    """
    digits = [int(num) for num in string]
    halfway = int(len(digits) / 2)
    return sum(num_1 + num_2 for num_1, num_2 in zip(digits, digits[halfway:]) 
                if num_1 == num_2)

assert sum_halfway_digits('1212') == 6
assert sum_halfway_digits('1221') == 0
assert sum_halfway_digits('123425') == 4
assert sum_halfway_digits('123123') == 12
assert sum_halfway_digits('12131415') == 4


if __name__ == "__main__":
    with open("day01_input.txt", 'r') as file:
        inputs = file.read().strip()
    print(sum_consecutive_digits(inputs))
    print(sum_halfway_digits(inputs))