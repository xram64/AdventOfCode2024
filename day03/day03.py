#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2024   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  3  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 159892596       |            #
#            |  `-----------'   Part 2: 92626942        |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

import re

def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


#╷----------.
#│  Part 1  │
#╵----------'
def Part1(input):
    return sum([int(mul[0])*int(mul[1]) for line in input for mul in re.findall(r"mul\((\d+),(\d+)\)", line)])


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(input):
    full_sum = 0
    
    # Wrap the program with `do()` and `don't()` commands to fully enclose all enabled instruction blocks.
    wrapped_input = "do()" + ' '.join(input) + "don't()"
    
    # Find all `do()...don't()` blocks in the program and scan the instructions within for `mul`s.
    for block in re.findall(r"do\(\)(.*?)don't\(\)", wrapped_input):
        full_sum += sum([int(mul[0])*int(mul[1]) for mul in re.findall(r"mul\((\d+),(\d+)\)", block)])
    
    return full_sum

if __name__ == "__main__":
    input = Setup('day03_input.txt')
    
    print(f"[Part 1] Resulting sum of `mul` instructions: {Part1(input)}")
    
    print(f"[Part 2] Resulting sum of enabled `mul` instructions: {Part2(input)}")