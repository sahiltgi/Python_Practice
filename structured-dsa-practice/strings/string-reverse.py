def stringreverse(str):
    sliced = str[::-1]
    reverse = ''.join(reversed(str))
    return [sliced, reverse]


if __name__ == "__main__":
    s = input('Enter value :- ')
    print(stringreverse(s))
