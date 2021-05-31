class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        return [[p for p in products if p[:i+1] == searchWord[:i+1]][:3] for i in range(len(searchWord))]
