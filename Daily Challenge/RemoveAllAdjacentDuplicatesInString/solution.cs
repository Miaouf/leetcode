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
    public string RemoveDuplicatesWithStack(string s) {
        
        var stack = new Stack<char>();
        var chars = s.ToCharArray();

        foreach (var c in chars) {
            if (stack.Count == 0) {
                stack.Push(c);
                continue;
            }

            if (stack.Peek() == c)
                stack.Pop();
            else
                stack.Push(c);
        }

        var result = new char[stack.Count];
        for (var i = stack.Count - 1; i >= 0; i--)
            result[i] = stack.Pop();

        return new string(result);
    }
}
