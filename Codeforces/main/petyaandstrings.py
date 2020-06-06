def comparison(string1,string2):
    str1 = string1.lower()
    str2 = string2.lower()
    if (str1 == str2):
        return 0
    elif str1 > str2:
        return 1
    else:
        return -1

if __name__ == "__main__":
    string1 = input()
    string2 = input()
    print(comparison(string1,string2))
