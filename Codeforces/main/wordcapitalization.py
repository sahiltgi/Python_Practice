def capitalization(string):
    if(len(string) < 10**3):
        return string[0].upper() + string[1:len(string)]
    return


if __name__ == "__main__":
    string = input()
    print(capitalization(string))
