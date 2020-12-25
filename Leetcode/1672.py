def maximumWealth(accounts):
    newARR = []
    for i in range(0,len(accounts)):
        a = sum(accounts[i])
        newARR.append(a)
    return max(newARR)


if __name__ == "__main__":
    accounts = [[1,5],[7,3],[3,5]]
    print(maximumWealth(accounts))