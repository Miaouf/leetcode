/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


void flatten(struct TreeNode* root){
    struct TreeNode* flatten_rec(struct TreeNode* root){
        if(root == NULL)
            return NULL;

        struct TreeNode* start = root;
        struct TreeNode* end = root->right;
        root->right = flatten_rec(root->left);
        root->left = NULL;
        while(root->right != NULL)
            root = root->right;

        root->right = flatten_rec(end);
        return start;
    }
    root = flatten_rec(root); 
}
