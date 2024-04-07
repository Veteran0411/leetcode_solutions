def groupAnagrams(s):
    a=[]
    anagrams={}
    for i in s:
        srt=sorted(i)
        if srt in a:
            anagrams[a.index(srt)].append(i)
        else:
            a.append(srt)
            anagrams[a.index(srt)]=[i]
    
    print(anagrams.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)