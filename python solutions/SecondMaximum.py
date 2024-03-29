a=[19,19,93,92,92,3,12,45,23]
maxi=a[0]
secondMaxi=0

trav=1

#bubble sort loop
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]


for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        a[trav]=a[i]
        trav+=1
print(a)

print("second maximum is: ",a[trav-2],trav)
# loop to find second largest number
# for i in a:
#     if i>maxi:
#         secMaxi=maxi
#         maxi=i
# print(secMaxi,maxi)

# convert to set and sort last second is sec max
# n=sorted(list(set(a)))
# print(n[-2])