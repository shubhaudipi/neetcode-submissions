class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for stri in strs:
            next = str(len(stri))
            res = res + next + "." + stri
        
        return res

    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        while index < len(s):
            numc = 0
            while s[index+numc] != ".":
                numc += 1
            length = int(s[index:(index+numc)])
            index += (numc + 1)
            res.append(s[index:(index+length)])
            index += length
        
        return res




