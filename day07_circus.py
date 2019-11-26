"""
https://adventofcode.com/2017/day/7
"""
import re
from typing import NamedTuple, List, Optional, Pattern, Iterator, Set  
from collections import Counter, defaultdict

aboves = List[str]

patt = re.compile("(?P<name>[a-z]+)\s\((?P<weight>[0-9]+)\)")

class Program(NamedTuple):
    name: str
    weight: int
    aboves: Optional[aboves] 

def process_line(line:str, pattern: Pattern) -> NamedTuple:
    """
    Parses the program name, weight and is aboves if exists
    otherwise empty string
    """
    parts = line.split("->")
    if len(parts) == 1:
        aboves = []
    else:
        aboves = [name.strip() for name in parts[1].split(',')]

    g = pattern.search(parts[0])

    return Program(name=g.group('name'), 
                   weight=int(g.group('weight')), 
                   aboves = aboves)

assert process_line(line="mmqyju (156) -> rjzvwv, noybkx", pattern=patt) ==  Program(name='mmqyju', weight=156, aboves=['rjzvwv', 'noybkx'])
assert process_line(line="mmqyju (156)", pattern=patt) ==  Program(name='mmqyju', weight=156, aboves=[])

def process_lines(lines:str, pattern: Pattern) -> Iterator[List[Program]]:
    for program in lines.split("\n"):
        yield process_line(program, patt)

def is_below(lines:str, pattern: Pattern) -> Set[str]:
    return set(program.name for program in process_lines(lines= lines, pattern = patt))

def is_above(lines:str, pattern: Pattern) -> Set[str]:
    return set(pgr for program in process_lines(lines= lines, pattern = patt) 
                   for pgr in program.aboves if program.aboves)

def base(lines:str, pattern: Pattern) -> str:
    aboves, belows = is_above(lines, pattern), is_below(lines, pattern)
    return list(belows.difference(aboves))[0]

TEST_INPUT ="""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft   
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

assert base(lines=TEST_INPUT, pattern=patt) =='tknk'

# could not resolve Part 2 
# example below copied from joel grus livecoding video
# personal note recurssion is still a pain
 

def balance_towers(programs_input: str):
    lookups = { program.name: program for program in process_lines(programs_input, pattern=patt) }
    
    def check(program: Program):
        """
        Return the total weight and is_balanced
        """
        #print("checking", program)
        subchecks = {name: check(lookups[name]) for name in program.aboves}
        subcheck_weights = {weight for weight, _ in subchecks.values()}
        is_balanced = len(subcheck_weights) <= 1
        weight = program.weight + sum(weight for weight, _ in subchecks.values())
        if len(subcheck_weights) > 1 and \
            all(is_balanced for _, is_balanced in subchecks.values()):
            print('program', program)
            for name, (total_weight, _) in subchecks.items():
                above_program = lookups[name]       
                print(name, f'total weight is {total_weight}', above_program.weight)
        #print(f'program is {program.name}', subchecks, subcheck_weights)
        return weight, is_balanced 

    root = lookups[base(programs_input, pattern=patt)]
    check(root)

#balance_towers(TEST_INPUT)

if __name__ == "__main__":
    with open("day07_input.txt", 'r') as file:
        puzzle_input = file.read()
        print(base(lines=puzzle_input, pattern=patt))
        print(balance_towers(puzzle_input))    

