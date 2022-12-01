def main():
    increased = 0

    # Open "data.txt"
    with open(r"Advent of Code\2021\1\data.txt") as file:
        data = file.readlines()
        data = [int(x) for x in data]

        for i in range(len(data)):
            if data[i] > data[i-1]:
                increased += 1
    
    print(increased)

if __name__ == "__main__":
    main()