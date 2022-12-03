if __name__ == '__main__':
    s = input()
    
    alnum = False
    alpha = False
    num = False
    lower = False
    upper = False

    for char in s:
        if char.isalnum():
            alnum = True

        if char.isalpha():
            alpha = True

        if char.isnumeric():
            num = True

        if char.islower():
            lower = True

        if char.isupper():
            upper = True

    print(alnum)
    print(alpha)
    print(num)
    print(lower)
    print(upper)
