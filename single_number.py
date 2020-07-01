from collections import Counter as c

def single_number(nums):
    res = c(nums).most_common()
    print(res)
    for i in res:
        if(i[1] == 1):
            return i[0]
    
nums = [2,2,1]
#nums = [4,1,2,1,2]

print(single_number(nums))