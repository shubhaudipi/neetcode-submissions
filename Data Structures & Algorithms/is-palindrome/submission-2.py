class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        fw = 0
        bw = len(s) - 1

        while fw < bw:
            while (fw<bw and (not s[fw].isalpha()) and (not s[fw].isdigit())):
                fw += 1
            
            while (fw<bw and (not s[bw].isalpha()) and (not s[bw].isdigit())):
                bw -= 1
            
            
            if s[fw] != s[bw]:
                return False
            fw += 1
            bw -= 1
        
        return True
        