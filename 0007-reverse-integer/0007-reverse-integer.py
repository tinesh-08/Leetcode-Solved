class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)
        res=0
        if x<0:
            res = 0-int(a[-1:0:-1])
        else:
            res = int(a[::-1])
        if res>pow(-2,31) and res<pow(2,31)-1:
            return res
        else:
            return 0