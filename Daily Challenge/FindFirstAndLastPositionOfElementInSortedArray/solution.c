int findLast(int* nums, int numsSize, int target, int offset) {
    while (offset < numsSize && target == nums[offset]) {
        offset++;
    }
    return offset-1;
}

int findFirst(int* nums, int numsSize, int target, int offset) {
    while (offset >= 0 && target == nums[offset]) {
        offset--;
    }
    return offset+1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    int* ret = malloc(sizeof(int)*2);
    *returnSize = 2;
    ret[0] = -1;
    ret[1] = -1;
    if (numsSize == 0) return ret;
    int inf = 0;
    int sup = numsSize - 1;
    
    int pivot = 0;
    
    while (inf <= sup && nums[pivot] != target) {
        pivot = (inf + sup) / 2;
        if (nums[pivot] > target) {
            sup = pivot-1;
        } else {
            inf = pivot+1;
        }
    }
    if (nums[pivot] != target) return ret;
    ret[0] = findFirst(nums,numsSize,target, pivot);
    ret[1] = findLast(nums,numsSize,target, pivot);
    return ret;
}
