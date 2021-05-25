operators = {
    "+" : lambda b,a : a+b,
    "-" : lambda b,a : a-b,
    "*" : lambda b,a : a*b,
    "/" : lambda b,a : int(a/b)
    
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in range(len(tokens)) :
            if(tokens[i] not in operators):
                nums.append(int(tokens[i]))
            else:
                nums.append(operators[tokens[i]](nums.pop(),nums.pop()))
        return nums[0]
