def the_sum():
    # a = 1
    # b = 1
    f1 = 1
    f2 = 1
    add = 0
    if (n < 1):
        return
    for x in range(0, n):
        add += f2
        next = f1 + f2
        f1 = f2
        f2 = next
    return add
    # add = 2
    # if k <= 1:
    #     return 0
    # elif k == 2:
    #     return a+b
    # else:
    #     for i in range(2,k):
    #         c = a + b
    #         add += c
    #         a = b
    #         b = c
    #     return add


if __name__ == "__main__":
    n = int(input())
    print(the_sum())