#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2024   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  1  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 1388114         |            #
#            |  `-----------'   Part 2: 23529853        |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

from collections import Counter


def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


#╷----------.
#│  Part 1  │
#╵----------'
def Part1(left_list, right_list):
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)
    
    distances = []
    for n in range(len(sorted_left_list)):
        distances.append(abs(sorted_left_list[n] - sorted_right_list[n]))
    
    return sum(distances)


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(left_list, right_list):
    # Similarity score: Number of times each number from the left list appears in the right list.
    # Total similarity score: Sum of products of each number in the left list with its similarity score.
    
    # Equivalently, given a unique number that appears in the left list, multiply the number, its multiplicity in
    #  the left list, and its multiplicity in the right list, and sum these products for the total similarity score.
    
    total_sim_score = 0
    
    left_counts = Counter(left_list)
    right_counts = Counter(right_list)
    
    for left_num in set(left_list):
        total_sim_score += left_num * left_counts[left_num] * right_counts[left_num]
    
    return total_sim_score


if __name__ == "__main__":
    input = Setup('day01_input.txt')
    
    left_list, right_list = [], []
    
    for line in input:
        if not line.strip() == '':
            left_list.append(int(line.split('   ')[0]))
            right_list.append(int(line.split('   ')[1]))
    
    print(f"[Part 1] Total distance between lists: {Part1(left_list, right_list)}")
    
    print(f"[Part 2] Total similarity score: {Part2(left_list, right_list)}")