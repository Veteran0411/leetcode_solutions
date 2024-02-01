# 152. Maximum Product Subarray
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(nums):
    ans=nums[0]
    currMin=nums[0]
    currMax=nums[0]
    
    for num in nums[1:]:
        preMin=currMin
        preMax=currMax
        
        if num<0:
            currMin=min(preMax*num,num)
            currMax=max(preMin*num,num)
        else:
            currMin=min(preMin*num,num)
            currMax=max(preMax*num,num)
    return currMax
    
if __name__=="__main__":
    nums = [2,3,-2,4]
    # nums = [-2,0,-1]
    maxProduct(nums)