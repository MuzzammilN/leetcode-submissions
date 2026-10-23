class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
 
        for word in strs:
            freqs = freq(word)

            map[tuple(freqs)].append(word)
    
        return list(map.values())

def freq(word: str) -> list[int]:
    freqs = [0] * 26
    for i in word:
        freqs[ord(i) - ord("a")] += 1
    
    return freqs