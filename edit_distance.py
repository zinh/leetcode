def distance(a: str, b: str) -> int:
    '''
    calculate edit distance to transform from a to b
    '''
    def d(i, j):
        if i > j:
            return d(j, j) + 2*(i - j)
        if i == 1:
            pass
        if j == 1:
            pass
    return d(len(a), len(b))
