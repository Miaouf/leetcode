#define min(a,b) a<b?a:b

int countBinarySubstrings(char * s){
    int length = strlen(s);
    if(length == 1){
        return 0;
    }
    
    int ans = 0;
    int prev = 0;
    int ind = 1;
    
    for(int i = 1; i< length; i++){
        if(s[i] == s[i-1]){
            ind++;
        }else{
            ans += min(prev,ind);
            prev = ind;
            ind = 1;
        }
    }
    ans+=min(prev,ind);
    return ans;
}
