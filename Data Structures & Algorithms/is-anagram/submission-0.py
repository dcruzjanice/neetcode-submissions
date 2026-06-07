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

        

        
        