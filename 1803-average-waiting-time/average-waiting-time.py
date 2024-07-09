class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        
        n=len(c)
        twt=0.0+c[0][1]
        end=c[0][0]+c[0][1]
        for i in range(1,n):
            if(end>c[i][0]):
                twt=twt+end-c[i][0]+c[i][1]
                end=end+c[i][1]
            else:
                twt=twt+c[i][1]
                end=c[i][0]+c[i][1]

        return(twt/n)