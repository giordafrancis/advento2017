"""
https://adventofcode.com/2017/day/4
"""
# PART 1

from typing import List

def is_valid_passphrase(passphrase: str) -> bool:
    """
    Verifies if  passphrase has any duplicates
    """
    passphrase = passphrase.split()
    set_passphrase = set(passphrase)
    return len(passphrase) == len(set_passphrase)

assert is_valid_passphrase("aa bb cc dd ee") == True
assert is_valid_passphrase("aa bb cc dd aa") == False
assert is_valid_passphrase("aa bb cc dd aaa") == True

def total_valid_passphrases(inputs:List[str]) -> int:
    return sum(is_valid_passphrase(passphrase) for passphrase in inputs.split("\n") 
    if passphrase)

# PART 2

def is_not_anagram(passphrase: str) -> bool:
    """
    Verifies if  passphrase has any anagrams
    """
    passphrase = passphrase.split()
    set_passphrase = set("".join(sorted(chunk)) for chunk in passphrase)
    return len(passphrase) == len(set_passphrase)

assert is_not_anagram("abcde fghij") == True
assert is_not_anagram("a ab abc abd abf abj") == True
assert is_not_anagram("abcde xyz ecdab") == False
assert is_not_anagram("abcde xyz ecdab") == False
assert is_not_anagram("iiii oiii ooii oooi oooo") == True
assert is_not_anagram("oiii ioii iioi iiio") == False


def total_valid_passphrases2(inputs:List[str]) -> int:
    return sum(is_not_anagram(passphrase) for passphrase in inputs.split("\n") 
    if passphrase)


if __name__ == "__main__":
    with open('day04_input.txt', 'r') as file:
        inputs = file.read()
        print(total_valid_passphrases(inputs))
        print(total_valid_passphrases2(inputs))
