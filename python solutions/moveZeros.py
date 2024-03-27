a=[0,0,0,12,2,3,4,0,]
j=0
for i in a:
    if i!=0:
        a[j]=i
        j+=1
        
for i in range(j,len(a)):
    a[i]=0
print(a)