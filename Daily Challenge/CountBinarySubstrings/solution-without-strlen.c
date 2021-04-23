int countBinarySubstrings(char * s){
    if (s[1] == '\0') return 0;
    int res = 0;
    int consecutiveBefore = 0;
    int consecutiveAfter = 0;
    
    int i = 0;
    char* curr = s[i];

    // first iteration
    while(s[i] != '\0' && curr == s[i]) {
        consecutiveBefore++;
        i++;
    }
    // then we just have to compute what comes after
    while(s[i] != '\0') {
        curr = s[i];
        while(s[i] != '\0' && curr == s[i]) {
            consecutiveAfter++;
            i++;
        }
        res += (consecutiveBefore < consecutiveAfter)?consecutiveBefore:consecutiveAfter;
        consecutiveBefore = consecutiveAfter;
        consecutiveAfter = 0;
    }
    return res;
}
