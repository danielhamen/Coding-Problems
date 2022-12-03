if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    arr = sorted(arr, key=lambda t: t[1])
    second = [i[1] for i in arr if i[1] > arr[0][1]][0]
    names = sorted([x[0] for x in arr if x[0] in [y[0] for y in arr if y[1] == second] and x[1] == second])
    
    print(
        "\n".join(names)
    )
