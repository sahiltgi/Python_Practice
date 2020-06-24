def word(string):
    countUp = 0
    countLo = 0
    for i in string:
        if(i.isupper()):
            countUp += 1
        else:
            countLo += 1
    if countUp > countLo:
        return string.upper()
    else:
        return string.lower()


if __name__ == "__main__":
    string = input()
    print(word(string))
