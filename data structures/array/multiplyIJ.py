def multiply(row, col, arr):
    for i in range(row):
        for j in range(col):
            arr[i][j] = i*j
    return arr


if __name__ == "__main__":
    row = int(input("enter the number of rows: "))
    col = int(input("enter the number of cols: "))
    arr = [[0 for i in range(col)] for j in range(row)]
    print(multiply(row, col, arr))
