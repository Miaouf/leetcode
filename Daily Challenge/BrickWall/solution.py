class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        dic = {}
        
        for i in range(height):
            for j in range(len(wall[i])-1):
                wall[i][j] += wall[i][j-1] if j!= 0 else 0
                if(wall[i][j] in dic):
                    dic[wall[i][j]]+=1
                else:
                    dic[wall[i][j]] = 1
      
        if(dic == {}):
            return height
        else:
            return height-dic[max(dic, key=dic.get)]
            
