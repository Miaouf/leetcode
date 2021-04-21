/* What could have happened if you try to do it recursively ?
* Well if you compute the complexity, you will have something in O(2^n)
* where n is the row number
* As expected, this code pass 42 tests but not the last one for n = 196
*/

#define min(x,y) (x < y ? x : y)

int minimumTotalRec(int** triangle, int size, int offset, int index) {
    if (offset >= (size-1)) {
        // last triangle
        return triangle[offset][index];
    } else {
        // between first and last triangle
        return triangle[offset][index] + min(minimumTotalRec(triangle, size, offset+1,index),minimumTotalRec(triangle, size, offset+1,index+1));
    }
}

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize){
    int res = triangle[0][0]; // hedge
    if (triangleSize == 1) return res;
    res += min(minimumTotalRec(triangle, triangleSize, 1,0),minimumTotalRec(triangle, triangleSize, 1,1));
    return res;
}

/* One-line version for C masters */
/*
int minimumTotalRec(int** triangle, int size, int offset, int index) {
  return (offset >= (size-1))?triangle[offset][index]:triangle[offset][index] + min(minimumTotalRec(triangle, size, offset+1,index),minimumTotalRec(triangle, size, offset+1,index+1));
}

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize){
    return (triangleSize == 1)?triangle[0][0]:triangle[0][0]+min(minimumTotalRec(triangle, triangleSize, 1,0),minimumTotalRec(triangle, triangleSize, 1,1));
}
*/
