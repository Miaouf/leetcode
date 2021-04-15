/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int max(int a, int b) {
    return (a > b)?a:b;
}

int findDeepestLeaves(struct TreeNode* root, int depth) {
    if (root == NULL) {
        return depth;
    }
    if (root->left == NULL && root->right == NULL) {
        return depth;
    }
    return max(findDeepestLeaves(root->left,depth+1),findDeepestLeaves(root->right,depth+1));
    
}
int deepestLeavesRec(struct TreeNode* root, int currentDepth, int maxDepth) {
    if (root == NULL) {
        return 0;
    }
    if (root->left == NULL && root->right == NULL) {
        if (currentDepth == maxDepth) {
            return root->val;
        } else {
            return 0;
        }
    }
    return deepestLeavesRec(root->left,currentDepth+1,maxDepth) + deepestLeavesRec(root->right,currentDepth+1,maxDepth);
}

int deepestLeavesSum(struct TreeNode* root){
    return deepestLeavesRec(root,0,findDeepestLeaves(root,0));
}
