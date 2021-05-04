bool checkPossibility(int* nums, int numsSize){
    if (numsSize < 2) return true;
    
    // we do the first iteration outside the for loop
    int numberToChange = 0;
    int curr,next;
    if (nums[0] > nums[1]) {
        numberToChange++;
    }
    
    for(int i = 1; i < numsSize-1; i++) {
        curr = nums[i];
        next = nums[i+1];
        // if already sorted we go next
        if (curr <= next) continue;
        // otherwise there will be one modif
        if (++numberToChange > 1) return false;
        // nums[i-1] is a candidate to be the new nums[i] value
        if (nums[i-1] <= next) continue;
        else {
            // or we change the i+1 to be equal to the i
            nums[i+1] = curr;
        }
    }
    return numberToChange <= 1;
}
