def main():
    elves = [[]]

    # Puzzle input is the same as #1:
    with open(r"2022\1\data.txt", "r") as data:
        data = data.readlines()
        for line in data:
            if line == "\n":
                elves.append([])
            else:
                elves[-1].append(int(line))
    
    elves = [sum(x) for x in elves]
    top_three = sorted(elves, reverse=True)[:3]
    top_three = sum(top_three)

    print(top_three)

if __name__ == "__main__":
    main()
