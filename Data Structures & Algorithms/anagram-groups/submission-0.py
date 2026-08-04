class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}
        for word in strs:
            letters = tuple(sorted(word))
            if letters in anagrams:
                anagrams.get(letters).append(word)
            else: 
                anagrams[letters] = [word]
        
        for key in anagrams:
            result.append(anagrams.get(key))
        
        return result