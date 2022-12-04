class Solution:
    def __init__(self, data_file:str = r"Advent of Code\2022\Day 1\data.txt"):
        # Load the data file:
        self.data = None
        with open(data_file, "r") as file:
            self.data = file.readlines()
    
    def __str__(self):
        return str(self.AOC())

    def AOC(self) -> int:
        """
        Solves Part B of the 1st Advent of Code Problem
        """
        
        elves = [[]]

        for line in self.data:
            if line == "\n":
                elves.append([])
            else:
                elves[-1].append(int(line))
        
        elves = [sum(x) for x in elves]
        top_three = sum(sorted(elves, reverse=True)[:3])

        return top_three

if __name__ == "__main__":
    print(Solution())

    # Correct Solution: 210367