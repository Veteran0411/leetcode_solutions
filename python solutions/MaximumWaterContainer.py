def maxArea(self, height: List[int]) -> int:
    counter=len(height)-1
    start=0
    end=len(height)-1
    a=[]
    while end>=start:
        a.append(min(height[start],height[end])*counter)
        if height[start]<=height[end]:
            start+=1
        else:
            end-=1
        counter-=1
    return max(a)
