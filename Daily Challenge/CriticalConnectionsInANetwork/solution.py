class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        ans = []
        
        for i,j in connections:
            dic[i].append(j)
            dic[j].append(i)
        
        time = [0]
        ind = [-1]*n
        low = [-1]*n
        
        def dfs(current,previous):
            ind[current] = low[current] = time[0]
            time[0] += 1
            
            for next in dic[current]:
                if(ind[next] == -1):
                    dfs(next,current)
                    low[current] = min(low[current],low[next])
                elif(next != previous):
                    low[current] = min(low[current],ind[next])
                
                if(low[next] > ind[current]):
                    ans.append([current,next])
                
        dfs(0,-1)
        print(ind,low)
        return ans
