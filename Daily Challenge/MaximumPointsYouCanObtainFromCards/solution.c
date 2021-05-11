int maxScore(int* cardPoints, int cardPointsSize, int k){
    int max_score = 0;
    for(int i = 0; i<k; i++){
        max_score += cardPoints[i];
    }
    
    int score = max_score;
    int start = k;
    int end = cardPointsSize;

    for(int i = 0; i<k; i++){
        score += (cardPoints[--end] - cardPoints[--start]);
        max_score = (score > max_score)?score:max_score;
    }
    return max_score;
}
