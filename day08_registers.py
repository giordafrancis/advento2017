"""
https://adventofcode.com/2017/day/8
"""

from typing import List, NamedTuple, Dict, Callable, Tuple, Iterator, DefaultDict
from collections import defaultdict
import operator

class Register(NamedTuple):
    """split between instruction variables/numbers and 
    condition variables/numbers
    """
    var_inst: str
    operator_inst: str 
    num_inst: int
    if_: str # so we can use tuple unpacking, 
    # condition variables and numbers below
    var_cond: str
    operator_cond: str
    num_cond: int


TEST_EXAMPLE ="""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

def process_line(text_in:str)->List[str]:
    return Register(*text_in.split())

def operators() -> Dict[str, Callable]:
    """
    Dict of operators callables 
    """
    operators = {}
    operators[">"] = operator.gt
    operators["<"] = operator.lt
    operators[">="] = operator.ge
    operators["<="] = operator.le
    operators["=="] = operator.eq
    operators["!="] = operator.ne
    operators["inc"] = operator.add
    operators["dec"] = operator.sub
    return operators

assert not operators()['>'](5,9)
assert operators()['=='](9,9)
assert operators()['!='](10,9)
assert operators()['inc'](10,-10) == 0
assert operators()['dec'](-10,-10) == 0

def register_logic(text_in: str) -> Tuple[int, int]:
    """
    Computes register logic
    returns max value for all variables
    """
    data: Iterator[Register] = (process_line(line) for line in text_in.split("\n"))
    variables: DefaultDict[str, int] = defaultdict(int)
    ops: Dict[str, Callable] = operators()
    highest_value: int = 0

    for reg in data:
        # condition logic i.e "if a < 1"
        if ops[reg.operator_cond](variables[reg.var_cond],
                                  int(reg.num_cond)):
            # if True compute instructions i.e "b inc(operator_inst) 5"
            variables[reg.var_inst] = ops[reg.operator_inst](variables[reg.var_inst], 
                                      int(reg.num_inst))
            highest_value = max(highest_value, max(variables.values()))
    return max(variables.values()), highest_value

assert register_logic(TEST_EXAMPLE)[0] == 1

if __name__ == "__main__":
    with open("day08_input.txt", 'r') as file:
        text_in = file.read()
        max_val, highest_value = register_logic(text_in)
        print("max value for part I:", max_val)
        print("highest value held for part II:", highest_value)
