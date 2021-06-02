public class Solution {
    public IList<int> MajorityElement(int[] nums) {
        Dictionary<int, int> occ = new Dictionary<int, int>();
        IList<int> res = new List<int>();
        int n = nums.Length;
        int majority = (n>2)?n/3:0;
        for(int i = 0; i < n; i++) {
            int tmp = nums[i];
            if (!occ.ContainsKey(tmp)) {
                occ.Add(tmp,1);
            } else {
                occ[tmp]++;
                
            }
            if (occ[tmp] > majority && !res.Contains(tmp)) {
                    res.Add(tmp);
            }
        }
        return res;
    }
}
