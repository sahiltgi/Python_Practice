def task(string):
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    final = ""
    for i in range(0,len(string)):
        if string[i] not in vowel:
            final += "."
            final += string[i]
    return final


if __name__ == "__main__":
    string = input().lower()
    print(task(string))
