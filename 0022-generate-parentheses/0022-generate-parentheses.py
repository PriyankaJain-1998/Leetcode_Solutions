class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def backtracking(openN, closeN):
            if openN==closeN==n: 
                res.append("".join(stack))
                return 

            if openN>closeN: 
                stack.append(")")
                backtracking(openN, closeN+1)
                stack.pop()

            if openN<n: 
                stack.append("(")
                backtracking(openN+1, closeN)
                stack.pop() 
        
        backtracking(0,0)
        return res