import pathlib 


DAY = 0

def read_file(day: int):
    file = pathlib.Path("data") / f"{day}.txt"
    with open(file, "r") as handle:
        lines = handle.readlines()
    return(lines)

def parse(lines, *, debug=False):
    pass

class Object:
    def __init__(self):
        pass
    
    def run_analysis(self, *, debug=False):
        pass
    
    def get_answer1(self, *, debug=False):
        return None

    def get_answer2(self, *, debug=False):
        return None
    
    def get_answers(self, *, debug=False):
        answer1 = self.get_answer1(debug=debug)
        answer2 = self.get_answer2(debug=debug)
        return answer1, answer2

if __name__ == "__main__":
    lines = read_file(DAY)
    object = parse(lines, debug=False)
    object.run_analysis(debug=False)
    answer1, answer2 = object.get_answers(debug=True)
    print(f"Answer 1: {answer1}\nAnswer 2: {answer2}")
