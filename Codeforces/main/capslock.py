def caps(string):
    small = string.lower()
    return small[0].upper() + small[1:]


if __name__ == "__main__":
    string = input()
    print(caps(string))
