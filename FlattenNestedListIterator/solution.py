# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    @staticmethod
    def nestedList_to_list(nestedList):
        L = []
        for i in nestedList:
            if(i.isInteger()):
                L.append(i.getInteger())
            else:
                L.extend(NestedIterator.nestedList_to_list(i.getList()))
        return L
    
    def __init__(self, nestedList: [NestedInteger]):
        self._L = self.nestedList_to_list(nestedList)
        self._i = 0
        self._n = len(self._L)

    
    def next(self) -> int:
        val = self._L[self._i]
        self._i += 1
        return (val)
    
    def hasNext(self) -> bool:
        return self._i < self._n
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
