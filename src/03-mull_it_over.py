import pathlib
import re


DAY = 3

REGEXP_MUL = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
REGEXP_NUMBER = r"[0-9]{1,3}"

def read_file(day: int):
    file = pathlib.Path("data") / f"{day}.txt"
    with open(file, "r") as handle:
        lines = handle.readlines()
    return(lines)

def parse(lines, *, debug=False):
    pattern_mul = re.compile(REGEXP_MUL)
    pattern_number = re.compile(REGEXP_NUMBER)
    mults = list()
    for line in lines:
        if debug:
            print(line)
        matches = pattern_mul.findall(line)
        if debug:
            print(matches)
        for match in matches:
            x, y = pattern_number.findall(match)
            mults.append(Mult(int(x), int(y)))
    return Object(mults)

class Mult():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

class Object:
    def __init__(self, mults):
        self.mults = mults
    
    def run_analysis(self, *, debug=False):
        self.sum_of_mults = sum(mult.mul() for mult in self.mults)
    
    def get_answer1(self, *, debug=False):
        return self.sum_of_mults

    def get_answer2(self, *, debug=False):
        return None
    
    def get_answers(self, *, debug=False):
        answer1 = self.get_answer1(debug=debug)
        answer2 = self.get_answer2(debug=debug)
        return answer1, answer2

test_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip()
def test():
    lines = test_input.splitlines()
    object = parse(lines, debug=True)
    object.run_analysis(debug=True)
    test1, test2 = object.get_answers(debug=True)
    print(f"Test 1: {test1}\nTest 2: {test2}")

if __name__ == "__main__":
    test()
    lines = read_file(DAY)
    object = parse(lines)
    object.run_analysis()
    answer1, answer2 = object.get_answers()
    print(f"Answer 1: {answer1}\nAnswer 2: {answer2}")
