def main():
    with open(r"2022\3\data.txt", "r") as file:
        data = file.readlines()
        sum = 0

        for line in data:
            # sum += _1(line)

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

            # print(amount)
            # exit()
            sum += amount
    
    print(sum)

if __name__ == "__main__":
    main()
