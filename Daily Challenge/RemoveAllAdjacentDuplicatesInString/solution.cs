public class Solution {
    public string RemoveDuplicates(string s) {
        string res = "";
        int cnt = 0;
        foreach (char c in s) {
            if (cnt == 0){
                res += c;
                ++cnt;
            } 
            else {
                if (res[cnt-1] == c) {
                    res = res.Remove(cnt-1,1);
                    --cnt;
                } else {
                    res += c;
                    ++cnt;
                }
            }
        }
        return res;
    }
}
