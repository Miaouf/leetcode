class MyCalendar:

    def __init__(self):
        self._event = []        

    def book(self, start: int, end: int) -> bool:
        for s, e in self._event : 

            if(start <= s and s < end):
                return False
            
            if(start < e and e <= end):
                return False
            
            if(s <= start and e >= end):
                return False
            
        self._event.append([start,end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
