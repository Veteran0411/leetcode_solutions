# aGiven a set of numbers remove all the
# occurances of a particular number.
# (Visteon, Persistent)
a=[1,2,2,3,4,6,6,7]
j=0
for i in a:
    if i==6:
        pass
    else:
        a[j]=i
        j+=1
for i in range(j):
    print(a[i],end=" ")
