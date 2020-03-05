def bubble_sort(lis):
    for i in range(len(lis)):
        for j in range(0, len(lis) - 1 - i):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
            print(lis)


lis = input("Enter the list: ").split()
lis = [int(x) for x in lis]
bubble_sort(lis)
print(lis)