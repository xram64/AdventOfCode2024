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
#            |  `-----------'   Part 2: 531             |            #
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


def is_report_safe(report: tuple) -> bool:
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
    return is_safe

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
        
        # Mark this report safe or unsafe.
        reports[report] = is_report_safe(report)
    
    # Calculate stats and return.
    return {
        'qty_safe_reports': sum(reports.values()),
        'qty_total_reports': len(reports.values()),
        'reports': reports,
    }


#╷----------.
#│  Part 2  │
#╵----------'
def Part2(analyzed_reports):
    reports: dict[tuple, bool] = analyzed_reports['reports']
    
    reports_safe_with_dampener = dict()
    
    # Check each report marked unsafe to see if it becomes safe if one level is removed.
    for report, was_safe in reports.items():
        # If report was already marked safe, just mark it safe again.
        if was_safe:
            reports_safe_with_dampener[report] = True
            continue
        
        # Test remaining set of levels, dropping one at a time, to check if this report is safe under dampening.
        for drop_level in range(len(report)):
            test_report = list(report)
            test_report.pop(drop_level)
            test_report = tuple(test_report)
            
            if is_report_safe(test_report):
                # Mark this report safe or unsafe.
                reports_safe_with_dampener[report] = True
                break
        
        # If loop did not break, report is also not safe under dampening.
        else:
            reports_safe_with_dampener[report] = False
    
    # Calculate stats and return.
    return {
        'qty_safe_reports_with_dampener': sum(reports_safe_with_dampener.values()),
        'qty_total_reports_with_dampener': len(reports_safe_with_dampener.values()),
        'reports_with_dampener': reports_safe_with_dampener,
    }
             


if __name__ == "__main__":
    input = Setup('day02_input.txt')
    
    analyzed_reports = Part1(input)
    
    print(f"[Part 1] Number of safe reports: {analyzed_reports['qty_safe_reports']} / {analyzed_reports['qty_total_reports']}")
    
    print(f"[Part 2] Number of safe reports with dampener: {Part2(analyzed_reports)['qty_safe_reports_with_dampener']} / {Part2(analyzed_reports)['qty_total_reports_with_dampener']}")