import pathlib
import re


DAY = 3

REGEXP_MUL = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
REGEXP_NUMBER = r"[0-9]{1,3}"
REGEXP_DO = r"don\'t.*do"

def read_file(day: int):
    file = pathlib.Path("data") / f"{day}.txt"
    with open(file, "r") as handle:
        lines = handle.readlines()
    return(lines)

def parse(lines, *, debug=False, part2=False):
    mults = list()    
    text = "\n".join(lines)
    if part2:
        pattern_disable = re.compile(REGEXP_DO)
        text = pattern_disable.sub("", text)
    if debug:
        print("Text being analysed: ", text)
    matches = re.findall(REGEXP_MUL, text)
    if debug:
        print("Matching", REGEXP_MUL, "matches found: ", matches)
    for match in matches:
        x, y = re.findall(REGEXP_NUMBER, match)
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
    
    def get_answer(self, *, debug=False):
        return self.sum_of_mults

test1_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip()
test2_input = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()
def test():
    lines1 = test1_input.splitlines()
    object1 = parse(lines1, debug=True)
    object1.run_analysis(debug=True)
    test1 = object1.get_answer(debug=True)
    lines2 = test2_input.splitlines()
    object2 = parse(lines2, debug=True, part2=True)
    object2.run_analysis(debug=True)
    test2 = object2.get_answer(debug=True)
    print(f"Test 1: {test1}\nTest 2: {test2}")

if __name__ == "__main__":
    test()
    lines = read_file(DAY)
    object1 = parse(lines)
    object1.run_analysis()
    answer1 = object1.get_answer()
    object2 = parse(lines, part2=True)
    object2.run_analysis()
    answer2 = object2.get_answer()
    print(f"Answer 1: {answer1}\nAnswer 2: {answer2}")
