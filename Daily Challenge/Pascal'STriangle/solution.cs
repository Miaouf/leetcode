public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        IList<IList<int>> res = new List<IList<int>>();
        IList<int> first = new List<int>();
        first.Add(1);
        res.Add(first);
        for(int i = 1; i < numRows; ++i) {
            IList<int> current = new List<int>();
            current.Add(res[i-1][0]);
            for(int j = 1; j < i; ++j) {
                current.Add(res[i-1][j-1] + res[i-1][j]);
            }
            current.Add(res[i-1][i-1]);
            res.Add(current);
        }
        return res;
    }
}
