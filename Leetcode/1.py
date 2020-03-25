# TWO SUM PROBLEM LEET CODE

def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return x,y


# if __name__ == "__main__":
nums = list(map(int,input().split()))
target = int(input())
print(twoSum(nums, target))
