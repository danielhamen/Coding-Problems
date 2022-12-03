import math

def priority(char:str) -> int:
    return ("abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()).index(char) + 1

def main():
    sum = 0

    with open(r"Advent of Code\2022\5\data.txt", "r") as data:
        data = data.readlines()
        for line in range(0, len(data), 3):
            line = [x.replace("\n", "") for x in data[line:line+3]]

            common_letter = [x for x in line[0] if x in line[1] and x in line[2]][0]

            sum += priority(common_letter)

    print(sum)

if __name__ == "__main__":
    main()