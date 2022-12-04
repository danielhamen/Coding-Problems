class Solution:
    def __init__(self, data_file:str = r"Advent of Code\2022\Day 4\data.txt"):
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
        Solves Part A of the 4th Advent of Code Problem
        """

        total = 0
        for pair in self.data:
            first,second = pair.split(",")

            second = second.replace("\n", "")

            first1,first2 = first.split("-")
            first_ = [x for x in range(int(first1), int(first2)+1)]

            second1,second2 = second.split("-")
            second_ = [x for x in range(int(second1), int(second2)+1)]

            count = 0
            for val in second_:
                if val in first_:
                    count += 1
            
            if count != len(second_):
                count = 0
                for val in first_:
                    if val in second_:
                        count += 1
                
                if count == len(first_):
                    total += 1
            
            else:
                total += 1
        
        return total

if __name__ == "__main__":
    print(Solution())

    # Correct Solution: 573