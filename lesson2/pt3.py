def maxProduct(nums):
    op = 0
    set=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            op=nums[i]*nums[j]
            set.append(op)
    print(max(set))

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
