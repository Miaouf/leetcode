int strStr(char * haystack, char * needle){
    int needleLen = strlen(needle);
    if(needleLen == 0) return 0;
    int haystackLen = strlen(haystack);
    if(haystackLen == 0 || haystackLen < needleLen) return -1;
    
    int i,j;
    for(i = 0; i < (haystackLen - needleLen + 1); i++) {
        for(j = i; j < haystackLen && j - i < needleLen; j++) {
            if (haystack[j] != needle[j-i]) break;
        }
        if ((j-i) == needleLen) return i;
    }
    return -1;
}
