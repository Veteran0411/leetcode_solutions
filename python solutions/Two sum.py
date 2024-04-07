# . Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# we search for remaining value in hashmap and if the remaining value in is hashmap we return (current index,and remaining value index)

def twoSum(nums,target):
    hashMap={}
    for index in range(len(nums)):
        remval=target-nums[index]
        if remval not in hashMap:
            hashMap[nums[index]]=index
        else:
            return [hashMap[remval],index]

nums=[3,2,4]
target=6
print(f"target:{target}\narray:{nums}")
print(twoSum(nums,target))