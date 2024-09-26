a=1
b=1
c=a+b
s=[1,1]
i=2
if(i>=3):
    s.append(c)
while(i<n):
    a=b
    b=a
    c=a+b
    s.append(c)
sum=0
for i in range(n):
    sum=sum+s[i]

print(sum)