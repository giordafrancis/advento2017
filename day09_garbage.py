"""
https://adventofcode.com/2017/day/9
"""

from typing import Tuple

def stream_processing(stream: str) -> Tuple[int, int]:
    depth = 0
    total_score = 0
    skip = False # for the next char after "!"
    garbage = False
    garbage_chars = 0
            
    for char in stream:
        #print ("char->", char, "depth->", depth, "total_score->", total_score, "garbage->", garbage)
        #print(garbage_chars)    
        if skip:
            skip = False
            continue
        elif char == "!":
            skip = True              
        elif garbage: # garbage always terminates according to rules
            garbage_chars += 1   
            if char == ">":
                garbage_chars -= 1
                garbage = False
        elif char == "<":
            garbage = True
        elif char == "{":
            depth += 1
            total_score += depth
        elif char == "}":
            depth -= 1
        
            
    return total_score, garbage_chars 


assert stream_processing("{}")[0] == 1
assert stream_processing("{{{}}}")[0] == 6
assert stream_processing("{{},{}}")[0] == 5
assert stream_processing("{{{},{},{{}}}}")[0] == 16
assert stream_processing("{<a>,<a>,<a>,<a>}")[0] == 1
assert stream_processing("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
assert stream_processing("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
assert stream_processing("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3

assert stream_processing("<>")[1] == 0
assert stream_processing("<<<<>")[1] == 3
assert stream_processing("<{!>}>")[1] == 2
assert stream_processing("<!!!>>")[1] == 0
assert stream_processing("""<{o"i!a,<{i<a>""")[1] == 10
assert stream_processing("<random characters>")[1] == 17

if __name__ == "__main__":
    with open("day09_input.txt") as file:
        stream = file.read()
        part_1, part_2 = stream_processing(stream)
        print("part 1 total score is ->", part_1)
        print("part 2 non-canceled chars within garbage->", part_2)