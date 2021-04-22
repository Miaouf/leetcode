struct dic{
    int length;
    int key[10000];
    int val[10000];
};

int in_dic(struct dic* dic, int key){
    
    for(int k = 0; k<dic->length; k++){
        if(dic->key[k] == key){
            return k;
        }
    }
    return -1;
}

void add(struct dic* dic, int key){
    int ind = in_dic(dic,key);
    
    if(ind == -1){
        dic->key[dic->length] = key;
        dic->val[dic->length] = 1;
        dic->length++; 
    }else{
        dic->val[ind]++;
    }
}

int max_dic(struct dic* dic){
    int max_v = 0;
    
    for(int k = 0; k<dic->length; k++){
        if(dic->val[k] > max_v){
            max_v = dic->val[k];
        }
    } 
    
    return max_v;
}

int leastBricks(int** wall, int wallSize, int* wallColSize){
    struct dic dict;
    dict.length = 0;
    int val[20000];

    for(int i = 0; i<wallSize; i++){
        for(int j = 0; j<wallColSize[i]-1; j++){
            wall[i][j] +=(j!=0? wall[i][j-1] : 0);
            add(&dict,wall[i][j]);
        }
    }
    
    return wallSize-max_dic(&dict);
}
