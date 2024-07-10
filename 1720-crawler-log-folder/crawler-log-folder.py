class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=1
        log=["main"]
        for i in range(len(logs)):
            if(logs[i]=="./" or (logs[i]=="../" and count==1)):
                continue
            elif (logs[i]=="../" and count>1):
                log.pop()
                count-=1
            else:
                log.append(logs[i])
                count+=1
        return len(log)-1
