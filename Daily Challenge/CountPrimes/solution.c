/* Not the best in time complexity but working */
int countPrimes(int n){
    if (n < 3) return 0;
    /* allocating and setting memory to zero (zero is True for us) */
    int* isNotPrime = calloc(n,sizeof(int));
    int count = 0;
    for (int i = 2; i < n; i++) {
        if (isNotPrime[i]) continue;
        count++;
        for (int j = i; j < n; j += i) {
            isNotPrime[j] = 1;
        }
    }
    free(isNotPrime);
    return count;
}
