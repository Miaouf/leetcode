#define MIN(x,y) (x<y)?x:y

int trap(int* height, int heightSize){
    int ret = 0;
    int min,sum,dep,depindex,maxnext, maxnextIndex;
    // we compute water trapped for each wall
    for(int i = 0; i < heightSize - 2; i++) {
        if (height[i] == 0) continue;
        dep = height[i];
        depindex=i+1;
        maxnextIndex = i+1;
        maxnext = 0;
        // we search for the next wall >= at our current wall
        while( depindex < heightSize && height[depindex] < dep) {
            // we store the max height and its index
            if (height[depindex] >= maxnext) 
            {
                maxnext = height[depindex];
                maxnextIndex = depindex;
            }
            depindex++;
        }
        // if we reached the end
        if (depindex == heightSize) {
            // we set the next wall to the max found before reaching the end
            depindex = maxnextIndex;
        }
        // we compute the min height between both walls
        min = MIN(height[depindex],height[i]);
        // maximal water trapped value
        sum = min*(depindex-i-1);
        // we remove each height from the sum above
        for(int j = (i+1); j < depindex; j++) {
            sum -= height[j];
        }
        // we add it only if the sum is positive
        if (sum > 0) ret+= sum;
        // we computed a trap so we go directly to next border
        i = depindex-1;
    }
    return ret;
}
