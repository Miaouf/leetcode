public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int, int> occ = new Dictionary<int, int>();
        int res = 0;
        int max = 0;
        int n = nums.Length;
        int majority = n/2;
        for(int i = 0; i < n; i++) {
            int tmp = nums[i];
            if (!occ.ContainsKey(tmp)) {
                occ.Add(tmp,1);
                if (max == 0) {
                    max = 1;
                    res = tmp;
                }
            } else {
                occ[tmp]++;
                if (occ[tmp] > max) {
                    max = occ[tmp];
                    res = tmp;
                    if (occ[tmp] > majority) {
                        break;
                    }
                }
            }
        }
        return res;
    }
}
