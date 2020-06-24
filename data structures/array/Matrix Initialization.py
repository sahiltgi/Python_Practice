def matrixInitialization(n):
    # this is done using array
    # ar = [[0]*n]*n
    # It's going to reuse the list, so each [[0]*n] index gets updated
    # ar = [[0 for i in range(n)] for j in range(n)]
    # It is not going to reuse the list so the index provided will  only be updated
    # ar[0][0] = 5
    # this is how we can update the matrix index value
    # print(ar)

    # can be done using dictionary
    dc = {}
    dc = {(i, j): 0 for i in range(n) for j in range(n)}
    print(dc)


if __name__ == "__main__":
    n = int(input("enter the n: "))
    matrixInitialization(n)
