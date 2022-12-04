class Solution:
    def __init__(self, data_file:str = r"Advent of Code\2022\Day 1\data.txt"):
        # Load the data file:
        self.data = None
        with open(data_file, "r") as file:
            self.data = file.read()
    
    def __str__(self):
        return str(self.AOC())

    def AOC(self) -> int:
        """
        Solves Part A of the 1st Advent of Code Problem
        """

        return max([sum(list(map(int, y))) for y in [x.split("\n") for x in self.data.split("\n\n")]])

if __name__ == "__main__":
    print(Solution())

    # Correct Solution: 72478