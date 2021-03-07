def maxProduct(nums):
    max = 0
    op = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            op=nums[i]*nums[j]
            if op > max:
                max = op
    print(max)

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])


