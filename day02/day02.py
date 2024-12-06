#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2024   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  2  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 479             |            #
#            |  `-----------'   Part 2:                 |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

from enum import Enum

class dir(Enum):
    UP = 1
    CONSTANT = 0
    DOWN = -1


def Setup(filename):
    with open(filename) as f:
        input = f.readlines()
    return [line.strip() for line in input]


#╷----------.
#│  Part 1  │
#╵----------'
def Part1(input):
    # A report is 'safe' if:
    #   - The levels are either all increasing or all decreasing.
    #   - Any two adjacent levels differ by at least one and at most three.
    
    reports = dict()
    
    for report in input:
        # Format reports, filtering out empty lines.
        if report.strip() != '':
            report = tuple(int(i) for i in report.split())
        else:
            continue
        
        # Scan across levels to check if this report is safe.
        is_safe = True
        last_level = None
        direction = None
        for this_level in report:
            # Determine direction (increasing/decreasing).
            if (direction is None) and (last_level is not None):
                direction = dir.CONSTANT if this_level == last_level else (dir.UP if (this_level > last_level) else dir.DOWN)
            
            # Test report for safeness.
            if (last_level is not None) and (
                # If any of these conditions pass, the report is unsafe:
                not (1 <= abs(this_level - last_level) <= 3) or         # Level difference outside of safe range
                direction == dir.UP and this_level < last_level or      # Levels changed direction (↗↘)
                direction == dir.DOWN and this_level > last_level or    # Levels changed direction (↘↗)
                direction == dir.CONSTANT                               # Level did not change
            ):
                is_safe = False
                break
            
            last_level = this_level
        
        # Mark this report safe or unsafe.
        reports[report] = is_safe
    
    # Calculate stats and return.
    return {'qty_safe_reports': sum(reports.values()), 'qty_total_reports': len(reports.values()), 'reports': reports}


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(input):
    ...


if __name__ == "__main__":
    input = Setup('day02_input.txt')
    
    print(f"[Part 1] Number of safe reports: {Part1(input)['qty_safe_reports']} / {Part1(input)['qty_total_reports']}")
    
    # print(f"[Part 2] : {Part2(input)}")