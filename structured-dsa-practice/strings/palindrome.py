def palindrome(str):
    return str == "".join(reversed(str))


if __name__ == "__main__":
    s = input('Enter value :- ')
    print(palindrome(s))