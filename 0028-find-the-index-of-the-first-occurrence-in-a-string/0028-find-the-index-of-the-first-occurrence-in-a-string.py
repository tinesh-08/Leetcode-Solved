class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            a=len(needle)
            b=len(haystack)
            if a==1 and b==1:
                return 0
            for i in range(len(haystack)-a+1):
                if needle==haystack[i:i+a]:
                    return i
        else:
            return -1