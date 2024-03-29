# 414. Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
nums = [3,2,1]
distintNum=sorted(set(nums))
print(distintNum[-3] if len(distintNum)>2 else distintNum[-1])