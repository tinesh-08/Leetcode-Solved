class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        t=1
        while t<n:
            s+="*"
            cur=s[0]
            p=0
            w=""
            for i in s:
                if i==cur:
                    p+=1
                else:
                    w+=str(p)+cur
                    cur=s[s.index(i)]
                    p=1
            s=w
            t+=1
        return s