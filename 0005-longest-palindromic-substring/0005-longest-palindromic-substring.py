class Solution:
    def longestPalindrome(self, s: str) -> str:
        a=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                t=s[i:j]
                if t==t[::-1]:
                    if len(t)>len(a):
                        a=t
        return a
