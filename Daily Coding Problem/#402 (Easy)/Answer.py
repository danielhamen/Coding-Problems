StrobogrammaticNumbers = ["0", "1", "8", "6", "9"]

def isStrobogrammatic(Number:int) -> bool:
    """
    If `Number` is strobogrammatic, the program will return True, else: False
    """

    for Char in str(Number):
        if Char not in StrobogrammaticNumbers:
            return False
    
    if str(Number)[::-1] != str(Number):
        return False

    return True

def getStrobogrammaticNumbers(n:int) -> list:
    """
    View Question in `Question.md`
    """

    Numbers = []

    for i in range(n):
        if isStrobogrammatic(i):
            Numbers.append(i)
    
    return Numbers