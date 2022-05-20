# # def findMedianSortedArrays(nums1, nums2):
# #     ... 


# nums1 = [1,2]
# nums2 = [3,4]

# nums1 +=nums2
# nums1.sort()
# print(len(nums1))
# c = len(nums1)//2
# print(nums1[c-1],nums1[c])

# d = (nums1[c-1] + nums1[c+1])/2
# print(d)

def findMedianSortedArrays(nums1,nums2):
    nums1 += nums2
    nums1.sort()

    if len(nums1)%2 == 0:
        c = len(nums1)//2
        # print("len c: ",c) # 2
        d = (nums1[c-1] + nums1[c])/2
        # print(nums1[c-1])

        return d
    else:
        c = len(nums1)//2
        d = nums1[c]
        return d

nums1=[1,2,3,4,5,6,7,8]
nums2 =[1,2,3,4]
print(findMedianSortedArrays(nums1,nums2))
    