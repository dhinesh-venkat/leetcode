def intersection(nums1,nums2):
    p1 = p2 = 0
    nums1, nums2 = sorted(nums1), sorted(nums2)
    res = []

    while True:
        try:
            if nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        except IndexError:
            break
    return res



# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1,nums2))