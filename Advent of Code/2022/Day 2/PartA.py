class Solution:
    def __init__(self, data_file:str = r"Advent of Code\2022\Day 2\data.txt"):
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
        Solves Part A of the 2nd Advent of Code Problem
        """

        sum = 0

        for line in self.data:
            elf,you = line.split()
            elf_ = "Z"
            if elf == "A":
                elf_ = "X"
            elif elf == "B":
                elf_ = "Y"

            bonus = 0
            if you == elf_:
                bonus = 3
            else:
                # Check if win:
                if you == "X": # Rock
                    if elf == "C":
                        bonus = 6
                elif you == "Y":
                    if elf == "A":
                        bonus = 6
                elif you == "Z":
                    if elf == "B":
                        bonus = 6

            amount = 3
            if you == "X": amount = 1
            elif you == "Y": amount = 2

            amount += bonus
            
            sum += amount
    
        return sum

if __name__ == "__main__":
    print(Solution())

    # Correct Solution: 13565