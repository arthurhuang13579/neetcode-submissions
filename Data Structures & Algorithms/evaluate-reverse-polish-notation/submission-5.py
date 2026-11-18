class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+": 0, "-": 1, "*": 2, "/": 3}

        stack = []

        for t in tokens:
            if t not in "+-*/":
                #print("Number add")
                stack.append(int(t))
                #print(stack)
            else:
                #print("Operation")
                first = stack.pop()
                second = stack.pop()
                #print(first)
                #print(second)
                result = 0
                
                if t == "+":
                    result = first + second
                elif t == "-":
                    result = second - first
                elif t == "*":
                    result = first * second
                else:
                    result = int(second / first)
                stack.append(result)
                #print(stack)
        return int(stack.pop())




        