def two_sum(nums,target):
    n = len(nums)
    if n <= 1:
        return -1
    var = 0
    for i in range(n):
        var = target - nums[i]
        for j in range(n-1,i,-1):
            if nums[j] == var:
                return [i,j]
            

nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))

