# make number postive reverse it multiply by -1 and then return the number
def reverseInteger(n):
    global flag
    flag=1
    rev=0
    if n<0:
        flag=0
        n*=-1
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev*-1 if flag==0 else rev
n=-123
print(reverseInteger(n))