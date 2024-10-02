class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x=str(bin(start))[2:]
        y=str(bin(goal))[2:]
        dif=abs(len(x)-len(y))
        p="0"*dif
        cnt=0
        if len(x)>len(y):
            y=p+y
        else:
            x=p+x
        for i in range(len(x)):
            if(x[i]!=y[i]):
                cnt+=1
        return cnt
