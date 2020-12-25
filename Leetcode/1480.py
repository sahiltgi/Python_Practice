def runningSum(nums):
    if len(nums) == 0:
        return
    elif len(nums) == 1:
        return nums
    elif len(nums) >= 2:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(runningSum(nums))
