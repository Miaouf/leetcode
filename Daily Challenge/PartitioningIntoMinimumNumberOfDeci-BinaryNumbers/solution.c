int minPartitions(char * n){
    int max = 0;
    int tmp;
    for (int i = 0; n[i] != '\0'; i++) {
        tmp = n[i] - '0';
        if (tmp > max) {
            max = tmp;
        }
        if (max == 9) break;
    }
    return max;
}
