def move_zeroes(nums):
    c = nums.count(0)
    nums[:] = [i for i in nums if i != 0]
    return nums + ([0] * c)

nums = [0,1,0,3,12]
#nums = [0,0,0,0,0,0,1,1]
#nums = [0]
print(move_zeroes(nums))