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
        Solves Part B of the 3rd Advent of Code Problem
        """

        sum = 0

        for line in range(0, len(self.data), 3):
            line = [x.replace("\n", "") for x in self.data[line:line+3]]

            common_letter = [x for x in line[0] if x in line[1] and x in line[2]][0]

            sum += self.priority(common_letter)

        return sum

    def priority(self, char:str) -> int:
        return ("abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()).index(char) + 1

if __name__ == "__main__":
    print(Solution())

    # Correct Solution: 2881