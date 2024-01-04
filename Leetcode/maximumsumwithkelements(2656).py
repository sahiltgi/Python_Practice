# MAXIMUM SUBARRAY

def maxSubArray(nums):
    current_max = global_max = nums[0]
    for i in range(1, len(nums)):
        current_max = max(nums[i], nums[i] + current_max)
        if current_max > global_max:
            global_max = current_max
    return global_max


if __name__ == "__main__":
    nums = list(map(int, input('Enter the value :-- ').split()))
    print(maxSubArray(nums))
