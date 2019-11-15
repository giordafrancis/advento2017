"""
https://adventofcode.com/2017/day/7
"""
import re
from typing import NamedTuple, List, Union, Pattern, Generic, Set  
from collections import namedtuple

aboves = List[str]

patt = re.compile("(?P<name>[a-z]+)\s\((?P<weight>[0-9]+)\)")

class program(NamedTuple):
    name: str
    weight: int
    aboves: Union[aboves, str] 

def process_line(line:str, pattern: Pattern) -> NamedTuple:
    """
    Parses the program name, weight and is aboves if exists
    otherwise empty string
    """
    parts = line.split("->")
    if len(parts) == 1:
        aboves = ""
    else:
        aboves = [name.strip() for name in parts[1].split(',')]

    g = pattern.search(parts[0])

    return program(name=g.group('name'), 
                   weight=int(g.group('weight')), 
                   aboves = aboves)

assert process_line(line="mmqyju (156) -> rjzvwv, noybkx", pattern=patt) ==  program(name='mmqyju', weight=156, aboves=['rjzvwv', 'noybkx'])
assert process_line(line="mmqyju (156)", pattern=patt) ==  program(name='mmqyju', weight=156, aboves="")

def process_lines(lines:str, pattern: Pattern) -> List[NamedTuple]:
    return (process_line(program, patt) for program in lines.split("\n"))

def is_below(lines:str, pattern: Pattern) -> Set[NamedTuple]:
    return set(program.name for program in process_lines(lines= lines, pattern = patt))

def is_above(lines:str, pattern: Pattern) -> Set[NamedTuple]:
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

with open("day07_input.txt", 'r') as file:
    print(base(lines=file.read(), pattern=patt))


