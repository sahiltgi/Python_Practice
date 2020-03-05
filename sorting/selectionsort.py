def selection_sort(lis):
    for i in range(0, len(lis) - 1):
        smallest = i
        for j in range(i+1, len(lis)):
            if lis[j] < lis[smallest]:
                smallest = j
        lis[i], lis[smallest] = lis[smallest], lis[i]


lis = input("Enter the array: ").split()
lis = [int(x) for x in lis]
selection_sort(lis)
print(lis)