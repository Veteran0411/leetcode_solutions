from collections import defaultdict

# my method
# def groupAnagrams(s):
#     a=[]
#     anagrams={}
#     for i in s:
#         srt=sorted(i)
#         if srt in a:
#             anagrams[a.index(srt)].append(i)
#         else:
#             a.append(srt)
#             anagrams[a.index(srt)]=[i]
#     print(anagrams.values())

def groupAnagrams(s):
    anagrams=defaultdict(list)
    for i in s:
        srt=tuple(sorted(i))
        anagrams[srt].append(i)
        
    print(list(anagrams.values()))
    
strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)