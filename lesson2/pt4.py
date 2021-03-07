def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target:
                return [i, j]

result=twoSum([2,11,7,15],9)
print(result)