class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x : x[1])
        ans = 0
        time = 0
        L_course = []
        
        for course in courses:
            if(time + course[0] <= course[1]):
                ans+=1
                time += course[0]
                heapq.heappush(L_course, -course[0])
                
            elif(L_course != []):
                if(- course[0] > L_course[0]):
                    time += heapq.heappop(L_course)
                    time += course[0]
                    heapq.heappush(L_course, -course[0])
                    
        return ans
