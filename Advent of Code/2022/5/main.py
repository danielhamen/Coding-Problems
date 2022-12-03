import math
import string

class AOC5:
    def __init__(self):
        # Gather the data:
        self.data = None
        with open(r"Advent of Code\2022\5\data.txt", "r") as data:
            self.data = data.readlines()

        # Get the answer to AOC #5
        self.output = self.main()

    def __str__(self):
        return str(self.output)

    @classmethod
    def priority(self, char:str) -> int:
        """
        Returns the index of `char` in the alphabet ( `[a-z][A-Z]` )
        """

        return string.ascii_letters.index(char) + 1
    
    def split_line(self, line:str) -> list[str, str]:
        """
        Returns the first, and second part of `line`
        """

        return line[:math.floor(len(line) / 2)],line[math.floor(len(line) / 2):]

    def main(self) -> int:
        return [[self.priority([x for x in self.split_line(line)[0] if self.split_line(line)[1].count(x) != 0][0])] for line in self.data]

        # sum = 0

        # for line in self.data:
        #     common_letter = [x for x in self.split_line(line[:-1])[0] if self.split_line(line[:-1])[1].count(x) != 0][0]

        #     sum += self.priority(common_letter)
    
        # return sum

if __name__ == "__main__":
    print(AOC5())