def printVertically(s):
    words = s.split(" ")

    height = max([len(x) for x in words])
    width = len(words)

    matrix = [['' for i in range(width)] for j in range(height)]

    row, col = 0, 0
    for x in words:
        for ch in x:
            matrix[row][col] = ch
            row += 1
        row = 0
        col += 1
    res = []

    for x in matrix:
        res.append("".join(x).rstrip())
    return res

s = "HOW ARE YOU"
print(printVertically(s))