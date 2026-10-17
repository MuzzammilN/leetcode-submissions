class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        an_map = {}

        if len(s) != len(t):
            return False

        for ch in s:
            an_map[ord(ch)] = an_map.get(ord(ch), 0) + 1

        for ch in t:
            an_map[ord(ch)] = an_map.get(ord(ch), 0) - 1

        for key in an_map:
            if an_map[key] > 0 or an_map[key] < 0:
                return False
    
        return True