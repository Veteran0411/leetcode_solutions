count=0
s=""
word1="123"
word2="456"
while count<len(word1+word2):
    if count<len(word1):
        s+=word1[count]
    if count<len(word2):
        s+=word2[count]
    count+=1

print(s)