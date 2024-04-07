import collections
dic={}
s="ssomling"

# def firstUniqueCharacter(s):
#     for i in s:
#         dic[i]=dic.get(i,0)+1
        
#     for i,j in dic.items():
#         if j==1:
#             print("first unique character is",i)
#             return s.index(i)
#     return -1
# print(firstUniqueCharacter(s)) 

print(dict(collections.Counter(s)))