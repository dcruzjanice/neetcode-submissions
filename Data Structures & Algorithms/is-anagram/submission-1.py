class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Scount = {}
        Tcount = {}
        if len(s) != len(t):
            return False
        for char in s:
            Scount[char] = Scount.get(char, 0) + 1

        for char in t:
            Tcount[char] = Tcount.get(char, 0) + 1

        return Scount == Tcount

        
#case 1: anagrams should hv same characters. so firstly if the no of chars in both strings 
#is diff then return false
#case 2: compare both strings bcz we need to see if each char occ in each string
#matches each char occ in secnond string. so we use dict for this for key value pairs 
#so char : freq pairs

        
        