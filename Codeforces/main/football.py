def football(string):
    dan0 = '0000000'
    dan1 = '1111111'
    if dan0 in string or dan1 in string:
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":
    string = input()
    print(football(string))
