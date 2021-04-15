  
int getOrd(char c, char * order) {
    for(int i = 0; i < 27; i++) {
        if (c == order[i]) return i;
    }
    return -1;
}

bool test(char * a, char * b, char * order) {
    int valA,valB;
    for(int i = 0; i < 21; i++) {
        if (a[i] == '\0' && b[i] != '\0') return true;
        if (b[i] == '\0' && a[i] != '\0') return false;
        if(a[i] == '\0' && b[i] == '\0') return true;
        if (a[i] == b[i]) continue;
        valA = getOrd(a[i],order);
        valB = getOrd(b[i],order);
        if (valA < valB) {
            return true;
        } else if (valA > valB) {
            return false;
        } else {
            continue;
        }
    }
    return true;
}

bool isAlienSorted(char ** words, int wordsSize, char * order){
    for(int i = 0; i < wordsSize - 1; i++) {
        if(!test(words[i],words[i+1],order)) return false;
    }
    return true;
}
