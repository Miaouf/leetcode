/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* preorder(struct Node* root, int* returnSize) {
    if(root == NULL){
        *returnSize = 0;
        return NULL;
    }
    
    int* L = malloc(sizeof(int)*10000);
    int ind = 0;
    
    struct Node* queue[1000];
    queue[0] = root;
    int ind_q = 1;
    
    struct Node* new_queue[1000];
    int ind_nq = 0;
    while(ind_q != 0){
        ind_nq = 0;
        root = queue[0];
        L[ind++] = root->val;
        for(int i = 0; i<(root->numChildren);i++){
            if(root->children[i] != NULL){
                new_queue[ind_nq++] = root->children[i];
            }
        }
        
        for(int k = 0; k < ind_q-1; k++){
           new_queue[ind_nq+k] = queue[k+1];
        }
        
        ind_q += ind_nq-1;
        
        for(int j = 0; j<ind_q;j++){
            queue[j] = new_queue[j];
        }
   
    }
    
    *returnSize = ind;
    return L;  
}
