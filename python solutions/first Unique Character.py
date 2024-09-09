import collections
dic={}
s="ssomoooling"

# def firstUniqueCharacter(s):
#     for i in s:
#         dic[i]=dic.get(i,0)+1
        
#     for i,j in dic.items():
#         if j==1:
#             print("first unique character is",i)
#             return s.index(i)
#     return -1
# print(firstUniqueCharacter(s)) 



# print(dict(collections.Counter(s)))
# print(dict(collections.Counter(s)))

def maxOccurance(s):
    for i in s:
        dic[i]=dic.get(i,0)+1
      
maxOccurance(s)  
print(max(dic,key=lambda k:dic[k])) 