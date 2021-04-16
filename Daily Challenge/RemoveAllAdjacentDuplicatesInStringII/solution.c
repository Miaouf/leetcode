void resize(char* s, int startIndex, int k, int len) {
    int i;
    for(i = startIndex; i < len && i+k < len; i++) {
        s[i] = s[i+k];
    }
    s[i] = '\0';
}

bool parseAndRemove(char *s, int k, int* len) {
    bool res = false;
    int i,j;
    for(i = 0; i < (*len - k + 1); i++) {
        j = 1;
        for(j = 1; (j < *len) && (j < k); j++) {
            if (s[i+j] != s[i]) break;
        }
        if (j == k) {
            resize(s,i,k,*len);
            res = true;
            *len-=k;
        }
    }
    return res;
}

char * removeDuplicates(char * s, int k){
    if (k == 0) return s;
    if (k == 1) return '\0';
    int len = strlen(s);
    while(parseAndRemove(s,k,&len));
    return s;
}
