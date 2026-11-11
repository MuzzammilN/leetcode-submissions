class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        
        subset = set()
        length = 0

        for r in range(len(s)):

            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            
            subset.add(s[r])
            length = max(length, len(subset))
            r += 1
            
        return length