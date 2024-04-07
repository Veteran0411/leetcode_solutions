def isAnagram(str1,str2):
    str1Copy=str1.lower()
    str2Copy=str2.lower()
    
    if len(str1Copy)!=len(str2Copy):
        return False
    anagram={}
    
    for i in str1Copy:
        anagram[i]=anagram.get(i,0)+1
    
    for i in str2Copy:
        if i not in anagram:
            return False
        anagram[i]-=1
        if anagram[i]<0:
            return False
    return True

str1="Hello"
str2="olleh"
print(isAnagram(str1,str2))