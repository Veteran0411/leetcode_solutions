# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
import collections
ransomNote="ab"
magazine="aabc"
ran = collections.Counter(ransomNote)
mag = collections.Counter(magazine)
print(ran,mag,len(ran-mag)) # takes only those characters which are there in ran, ignoring extra charaters in mag , we will not get negative value
print(len(ran - mag) == 0) # subtract mag from ran