class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else: 
            tset = set(t)
            sset = set(s)
            tdict = dict.fromkeys(tset, 0)
            sdict = dict.fromkeys(sset, 0)
            for i in range(len(s)):
                tdict[t[i]] += 1
                sdict[s[i]] += 1
        return tdict == sdict
                    

        