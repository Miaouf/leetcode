

int * mergeTwoList(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int * merged = malloc(sizeof(int) *(nums1Size + nums2Size));
    
    int index0 = 0;
    int index1 = 0;
    int index2 = 0;
    
    while(index1 < nums1Size && index2 < nums2Size) {
        if (nums1[index1] < nums2[index2]) {
            merged[index0] = nums1[index1];
            index0++;
            index1++;
        } else if (nums1[index1] > nums2[index2]) {
            merged[index0] = nums2[index2];
            index0++;
            index2++;
        } else {
            merged[index0] = nums1[index1];
            merged[index0+1] = nums2[index2];
            index0+=2;
            index1++;
            index2++;
        }
    }
    while (index1 < nums1Size) {
        merged[index0] = nums1[index1];
        index0++;
        index1++;
    }
    while (index2 < nums2Size) {
        merged[index0] = nums2[index2];
        index0++;
        index2++;
    }
    return merged;
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int * merged = mergeTwoList(nums1, nums1Size, nums2, nums2Size);
    int len = nums1Size + nums2Size;
    double sum = (len%2)?merged[len/2]:((double)merged[len/2-1] + (double)merged[len/2])/2;
    free(merged);
    return sum;
}
