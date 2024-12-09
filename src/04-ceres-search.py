import pathlib
import re


DAY = 4


def read_file(day: int):
    file = pathlib.Path("data") / f"{day}.txt"
    with open(file, "r") as handle:
        lines = handle.readlines()
    return(lines)

def parse(lines, *, debug=False):
    obj = Object(lines)
    print("No. of lines: ", obj.nrows)
    print("No. of columns: ", obj.ncols)
    return obj

class Object:
    def __init__(self, lines):
        self.left_to_right = lines
        self.nrows = len(lines)
        self.ncols = len(lines[0])

    def __str__(self):
        return "\n".join(self.left_to_right)
        
    def pad_out(self, *, debug=False):
        # .abc.
        # .def
        # ...
        # ..
        # .
        #
        # .abc.
        #  def.
        #   ...
        #    ..
        #     .
        #
        # add nrow-1 on both sides
        # and pad to a square:
        # with size = ncol + 2*(nrow - 1)
        # add empty columns to the left and right
        # which means adding characters to each row
        size = self.ncols + 2 * (self.nrows - 1)
        self.size = size
        extra_chars = "." * (self.nrows - 1)
        for index, row in enumerate(self.left_to_right):
            new_row = extra_chars + row + extra_chars
            self.left_to_right[index] = new_row
        # add empty rows to the bottom
        empty_row = "." * len(new_row)
        for _ in range(size - self.nrows):
            self.left_to_right.append(empty_row)         
        if debug:
            print(self)

    def populate_top_to_bottom(self, *, debug=False):
        self.top_to_bottom = list()
        for col_index in range(self.ncols):
            column = str()
            for index in range(self.nrows):
                line = self.left_to_right[index]
                char = line[col_index + self.nrows]
                column += char
            self.top_to_bottom.append(column)
        if debug:
            print(self.top_to_bottom)
    
    def populate_topleft_to_bottomright(self, *, debug=False):
        self.topleft_to_bottomright = list()
        if debug:
            print(f"{self.ncols=}, {self.nrows=}")
        for outer_index in range(self.size):
            characters = list()
            for inner_index in range(outer_index + 1):
                row_index = inner_index
                col_index = outer_index - inner_index
                character = self.left_to_right[row_index][col_index]
                if debug:
                    print(f"{outer_index=}, {inner_index=}, {character=}")
                characters.append(character)
            line = "".join(characters)
            self.topleft_to_bottomright.append(line)
        if debug:
            print(self.topleft_to_bottomright)

    def populate_topright_to_bottomleft(self, *, debug=False):
        self.topright_to_bottomleft = list()
        for outer_index in range(self.size):
            characters = list()
            for inner_index in range(outer_index + 1):
                row_index = inner_index
                col_index = self.size + inner_index - outer_index - 1
                character = self.left_to_right[row_index][col_index]
                characters.append(character)
            line = "".join(characters)
            self.topright_to_bottomleft.append(line)
        if debug:
            print(self.topright_to_bottomleft)
    
    def find_matches(self, *, regexp = "XMAS", regexp_rev = "SAMX", debug=False):
        pattern = re.compile(regexp)
        pattern_reverse = re.compile(regexp_rev)
        grids = [
            self.left_to_right,
            self.top_to_bottom,
            self.topleft_to_bottomright,
            self.topright_to_bottomleft,
        ]
        self.n_matches = 0
        for grid in grids:
            n_matches = 0
            for line in grid:
                matches_forward = pattern.findall( line)
                matches_reverse = pattern_reverse.findall(line)
                n_matches += len(matches_forward) + len(matches_reverse)
            self.n_matches += n_matches
            if debug:
                print(f"This grid has {n_matches=}")
    
    def run_analysis(self, *, debug=False):
        self.pad_out(debug=debug)
        self.populate_top_to_bottom(debug=debug)
        self.populate_topleft_to_bottomright(debug=debug)
        self.populate_topright_to_bottomleft(debug=debug)
        self.find_matches(debug=debug)
    
    def get_answer1(self, *, debug=False):
        return self.n_matches

    def get_answer2(self, *, debug=False):
        return None
    
    def get_answers(self, *, debug=False):
        answer1 = self.get_answer1(debug=debug)
        answer2 = self.get_answer2(debug=debug)
        return answer1, answer2

test_input = """
MMMSXXMASMo
MSAMXMSMSAo
AMXSXMAAMMo
MSAMASMSMXo
XMASAMXAMMo
XXAMMXXAMAo
SMSMSASXSSo
SAXAMASAAAo
MAMMMXMMMMo
MXMXAXMASXo
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
