import math
import string

class Solution:
    def __init__(self, data_file:str = r"Advent of Code\2022\Day 3\data.txt"):
        # Load the data file:
        self.data = None
        with open(data_file, "r") as file:
            self.data = file.readlines()

            # Remove the newlines:
            self.data = [x.replace("\n", "") for x in self.data]
    
    def __str__(self):
        return str(self.AOC())

    def AOC(self) -> int:
        """
        Solves Part A of the 3rd Advent of Code Problem
        """

        return sum(sum([[self.priority([x for x in self.split_line(line)[0] if self.split_line(line)[1].count(x) != 0][0])] for line in self.data], []))

    def split_line(self, line:str) -> list[str, str]:
        """
        Returns the first, and second part of `line`
        """

        return line[:math.floor(len(line) / 2)],line[math.floor(len(line) / 2):]

    def priority(self, char:str) -> int:
        """
        Returns the index of `char` in the alphabet ( `[a-z][A-Z]` )
        """

        return string.ascii_letters.index(char) + 1

if __name__ == "__main__":
    print(Solution())

    # Correct Solution: 7980