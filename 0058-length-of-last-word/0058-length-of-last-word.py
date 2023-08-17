class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=[x for x in s.split(" ") if len(x)>=1]
        if len(a)==0:
            s=s.replace(' ','')
            return len(s)
        return len(a[-1])