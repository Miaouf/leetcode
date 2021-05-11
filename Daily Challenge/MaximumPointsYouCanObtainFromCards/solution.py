class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score = sum(cardPoints[:k])
        score = max_score
        start = k
        end = 0
        
        for _ in range(k):
            start -= 1
            end -= 1
            score += (cardPoints[end] - cardPoints[start])
            max_score = max(max_score,score)
            
        return max_score    
