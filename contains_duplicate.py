from collections import Counter as c

def Contains_duplicate(nums):
    if not nums:
        return False
    res = c(nums).most_common(1)
    if res[0][1] == 1:
        return False
    return True

#nums = [1,1,1,3,3,4,3,2,4,2]
#nums = [1,2,3,4]
#nums = [1,2,3,1]
nums = []
print(Contains_duplicate(nums))
