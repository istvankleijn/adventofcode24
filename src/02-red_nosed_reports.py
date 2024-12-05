import pathlib


DAY = 2


def read_file(day: int):
    file = pathlib.Path("data") / f"{day}.txt"
    with open(file, "r") as handle:
        lines = handle.readlines()
    return(lines)

def parse(lines, *, debug = False):
    reports = list()
    for line in lines:
        levels = [int(s) for s in line.split(" ")]
        report = Report(levels)
        reports.append(report)
    return Reports(reports)


class Report:
    def __init__(self, levels):
        self.levels = levels
        self.nlevels = len(levels)
    
    def is_increasing(self):
        return self.levels == sorted(self.levels)
    
    def is_decreasing(self):
        return self.levels == sorted(self.levels, reverse=True)
    
    def is_ordered(self):
        return self.is_increasing() or self.is_decreasing()
    
    def adjacent_levels_between(self, min, max):
        for i in range(0, self.nlevels - 1):
            prev = self.levels[i]
            next = self.levels[i + 1]
            diff = abs(next - prev)
            if diff < min or diff > max:
                return False
        return True

    
    def is_safe(self):
        return self.is_ordered() and self.adjacent_levels_between(1, 3)

class Reports:
    def __init__(self, reports):
        self.reports = reports
    
    def run_analysis(self, *, debug=False):
        self.safety = [report.is_safe() for report in self.reports]
    
    def get_answer1(self, *, debug=False):
        return sum(self.safety)

    def get_answer2(self, *, debug=False):
        return None
    
    def get_answers(self, *, debug=False):
        answer1 = self.get_answer1(debug=debug)
        answer2 = self.get_answer2(debug=debug)
        return answer1, answer2

test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()
def test():
    lines = test_input.splitlines()
    object = parse(lines, debug=True)
    object.run_analysis(debug=True)
    report = object.reports[0]
    print(
        report,
        report.is_increasing(),
        report.is_decreasing(),
        report.is_ordered(),
        report.adjacent_levels_between(1, 3)
    )
    for report in object.reports:
        print(report.is_safe())
    test1, test2 = object.get_answers(debug=True)
    print(f"Test 1: {test1}\nTest 2: {test2}")

if __name__ == "__main__":
    test()
    lines = read_file(DAY)
    object = parse(lines)
    object.run_analysis()
    answer1, answer2 = object.get_answers()
    print(f"Answer 1: {answer1}\nAnswer 2: {answer2}")
