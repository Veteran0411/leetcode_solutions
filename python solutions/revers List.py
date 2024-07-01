def ReverseList(l):
    start=0
    end=len(l)-1
    while start<=end:
        l[start],l[end]=l[end],l[start]
        start+=1
        end-=1
if __name__=="__main__":
    l=[1,2,3,4,5]
    ReverseList(l)
    print(l)