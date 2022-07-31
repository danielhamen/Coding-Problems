def sum(L:list, i:int, j:int) -> float | int:
    """
    View Question in `Question.md`
    """

    ANS = 0
    
    for i in range(i, j):
        ANS += L[i]
    
    return ANS