public class MinStack {
    private int min;
    private int top;
    private bool isInitialized = false;
    private Stack<int> stack;
    /** initialize your data structure here. */
    public MinStack() {
        min = -1;
        stack = new Stack<int>();
    }
    
    public void Push(int val) {
        if (isInitialized) {
            if (val < min) {
                min = val;
            }
        } else {
            min = val;
            isInitialized = true;
        }
        stack.Push(val);
    }
    
    public void Pop() {
        int oldTop = stack.Peek();
        stack.Pop();
        if (min == oldTop && !stack.Contains(min)) {
            int[] array = stack.ToArray();
            if (array.Length > 0) {
                min = array.Min();
            } else {
                isInitialized = false;
            }
        }
    }
    
    public int Top() {
        return stack.Peek();
    }
    
    public int GetMin() {
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
