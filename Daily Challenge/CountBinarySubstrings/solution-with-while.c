int countBinarySubstrings(char * s){
    int len = strlen(s);
    if (len < 2) return 0;
    int res = 0;
    int consecutiveBefore = 0;
    int consecutiveAfter = 0;
    
    int i = 0;
    char* curr = s[i];

    // first iteration
    while(i < len && curr == s[i]) {
        consecutiveBefore++;
        i++;
    }
    // then we just have to compute what comes after
    while(i < len) {
        curr = s[i];
        while(i < len && curr == s[i]) {
            consecutiveAfter++;
            i++;
        }
        res += (consecutiveBefore < consecutiveAfter)?consecutiveBefore:consecutiveAfter;
        consecutiveBefore = consecutiveAfter;
        consecutiveAfter = 0;
    }
    return res;
}
