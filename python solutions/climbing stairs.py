# #same as fibonacci


# Code
# Testcase
# Test Result
# Test Result


# 70. Climbing Stairs
# Solved
# Easy
# Topics
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45\
    
class Solution():
    def __init__(self) -> None:
        print("created an instance of the class")
        return
    
    def climbingStairs(self,n):
        steps=[0]*(n+1)
        steps[0],steps[1]=1,1
        for i in range(2,n+1):
            steps[i]=steps[i-1]+steps[i-2]
        return steps[n]
    
#creating an instance
som=Solution()
n=int(input("enter the number of stairs: "))
ans=som.climbingStairs(n)
print(f"total stairs to climb: {ans}")



def fibo(n):
    if n==0 or n==1:
        return 1
    
    return fibo(n-1)+fibo(n-2)


print(fibo(5))




