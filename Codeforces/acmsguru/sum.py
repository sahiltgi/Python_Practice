# a,b = map(int,input().split())
# c = a + b
# print(c)

def productExceptSelf(nums):
    res = [1]

    for i in range(len(nums) - 1):
        res.append(res[-1] * nums[i])

    temp = nums[-1]
    for i in range(-2, -len(nums) - 1, -1):
        res[i] *= temp
        temp *= nums[i]


    return res

nums = [1,2,3,4]
print(productExceptSelf(nums))