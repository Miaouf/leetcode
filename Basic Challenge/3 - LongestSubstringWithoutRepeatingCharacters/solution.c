
int exist(char * s, int len, char c){
    for(int i = 0; i < len; i++) {
        if (s[i] == c) return true;
    }
    return false;
}

int lengthOfLongestSubstring(char * s){
    size_t len = strlen(s);
    if (len < 2) return (int)len;
    char seen[128];
    int seen_index = 0;
    int best = 0;
    int tmp = 0;
    for (size_t i = 0; i < len; i++){
        seen[seen_index] = s[i];
        seen_index++;
        tmp++;
        for(int j = i + 1; j < len; j++) {
            if (! exist(seen, seen_index, s[j])){
                seen[seen_index] = s[j];
                seen_index++;
                tmp++;
            } else {
                break;
            }
        }
        if (tmp > best) best = tmp;
        tmp = 0;
        seen_index = 0;
    }
    return best;
}
