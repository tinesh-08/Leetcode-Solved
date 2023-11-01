class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def StringForm(x,arr):
            def rever(a):
                return a[::-1]
            def inver(b):
                inverse_s = ''
                for i in b:
                    if i == '0':
                        inverse_s += '1'
                    else:
                        inverse_s += '0'
                return inverse_s

            x = arr[x-1] + "1" + rever(inver(arr[x-1]))
            arr.append(x)
            return arr
        
        arr=["0"]
        for i in range(1,n+1):
            if len(arr)<n:
                arr=StringForm(i,arr)
            else:
                t = arr[n-1]
                return t[k-1]
                