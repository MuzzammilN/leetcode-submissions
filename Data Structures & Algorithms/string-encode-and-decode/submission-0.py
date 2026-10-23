class Solution:
    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for word in strs:
            newStr += "#5" + word
        
        return newStr


    def decode(self, s: str) -> List[str]:
        newStr = s.strip().split("#5")
        return newStr[1:]