def main():
    elves = [[]]
    with open(r"data.txt", "r") as data:
        data = data.readlines()
        for line in data:
            if line == "\n":
                elves.append([])
            else:
                elves[-1].append(int(line))
    
    elves = [sum(x) for x in elves]
    max_cals = max(elves)

    print(max_cals)

if __name__ == "__main__":
    main()
