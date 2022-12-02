def main():
    sum = 0

    with open(r"2022\4\data.txt", "r") as data:
        for line line data.readlines():
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

    print(sum)

if __name__ == "__main__":
    main()
