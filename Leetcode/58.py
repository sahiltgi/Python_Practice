# LENGTH OF LAST WORD

def lengthOfLastWord(s: str) -> int:
    count = 0
    x = s.strip()
    for i in range(len(x)):
        if x[i] == " ":
            count = 0
        else:
            count += 1
    return count


if __name__ == "__main__":
    s = input()
    print(lengthOfLastWord(s))
