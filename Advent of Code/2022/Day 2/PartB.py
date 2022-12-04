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
        Solves Part B of the 2nd Advent of Code Problem
        """

        sum = 0
        for line in self.data:
            elf,end = line.split()
            bonus = 0
            if end == "X":
                bonus = 0

            elif end == "Y":
                bonus = 3

            elif end == "Z":
                bonus = 6

            amount = 0

            
            # Lose:
            you = ""
            if end == "X":
                if elf == "A":
                    you = "C"
                elif elf == "B":
                    you = "A"
                else:
                    you = "B"
            elif end == "Y":
                you = elf
            elif end == "Z":
                if elf == "A":
                    you = "B"
                elif elf == "B":
                    you = "C"
                else:
                    you = "A"

            if you == "A":
                amount += 1
            elif you == "B":
                amount += 2
            elif you == "C":
                amount += 3
                amount += bonus

            sum += amount
    
        return sum

if __name__ == "__main__":
    print(Solution())

    # Correct Solution: 12424