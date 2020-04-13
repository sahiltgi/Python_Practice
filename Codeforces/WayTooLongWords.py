def WayTooLongWords():
    lis = []
    if n >= 1 and n <= 100:
        for i in range(0, n):
            string = input()
            if len(string) > 10:
                lis.append(string[0] + str(len(string) - 2) + string[-1])
            else:
                lis.append(string)
        print(*lis, sep="\n")
    else:
        print("0")


if __name__ == "__main__":
    n = int(input())
    WayTooLongWords()
