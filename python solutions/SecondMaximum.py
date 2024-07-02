import copy
a=[19,19,93,92,92,3,12,45,23,99]
copyA=list(set(a))
maxi=copyA[0]
secondMaxi=0
trav=1

#bubble sort loop
for i in range(len(copyA)):
    for j in range(len(copyA)-1):
        if copyA[j]>copyA[j+1]:
            copyA[j],copyA[j+1]=copyA[j+1],copyA[j]


for i in range(1,len(copyA)):
    if copyA[i]!=copyA[i-1]:
        copyA[trav]=copyA[i]
        trav+=1
print(copyA)

print("second maximum is: ",copyA[trav-2])

# loop to find second largest number
# for i in a:
#     if i>maxi:
#         secMaxi=maxi
#         maxi=i
# print(secMaxi,maxi)

# convert to set and sort last second is sec max
# n=sorted(list(set(a)))
# print(n[-2])