def valUpdate(row, col):
    pass
    for i in range(2):
        for j in range(10):
            dc()


if __name__ == "__main__":
    row = int(input("enter the row count: "))
    col = int(input("enter the col count: "))
    dc = {}
    dc = {(i, j): 0 for i in range(col) for j in range(row)}
    print(dc)
    print(valUpdate(row,col))