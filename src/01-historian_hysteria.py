import collections
import pathlib


DAY = 1

def read_file(day: int):
    file = pathlib.Path("data") / f"{day}.txt"
    with open(file, "r") as handle:
        lines = handle.readlines()
    return(lines)

def parse(lines, *, debug = False):
    left_list = list()
    right_list = list()
    for line in lines:
        if debug:
            print(line)
        left, right = line.split()
        left_number = int(left)
        right_number = int(right)
        if debug:
            print(left_number, right_number)
        left_list.append(left_number)
        right_list.append(right_number)
    return HistoriansLists(left_list, right_list)

class HistoriansLists:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def sort_lists(self):
        self.left.sort()
        self.right.sort()
    
    def run_analysis(self, *, debug = False):
        if debug:
            print(
                "Before sorting: \n",
                "First 5 on left: ", self.left[:5], "\n",
                "First 5 on right: ", self.right[:5]
            )
        self.sort_lists()
        if debug:
            print(
                "After sorting: \n",
                "First 5 on left: ", self.left[:5], "\n",
                "First 5 on right: ", self.right[:5]
            )
    
    def get_distance(self, *, debug = False):
        distance = sum(
            abs(y - x) for x,y in zip(self.left, self.right, strict = True)
        )
        return distance
    
    def similarity_score(self):
        counts = collections.Counter(self.right)
        score = sum(x * counts[x] for x in self.left)
        return score
    
    def get_answer1(self, *, debug = False):
        return self.get_distance(debug = debug)

    def get_answer2(self, *, debug = False):
        return self.similarity_score()
    
    def get_answers(self, *, debug = False):
        answer1 = self.get_answer1(debug = debug)
        answer2 = self.get_answer2(debug = debug)
        return answer1, answer2

if __name__ == "__main__":
    lines = read_file(DAY)
    object = parse(lines, debug = False)
    object.run_analysis(debug = False)
    answer1, answer2 = object.get_answers(debug = True)
    print(f"Answer 1: {answer1}\nAnswer 2: {answer2}")
