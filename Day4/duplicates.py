nums=[1,1,2,3,4,5,6,5]
nums1=[]
for i in nums:
    if i not in nums1:
        nums1.append(i)
print(nums1)
