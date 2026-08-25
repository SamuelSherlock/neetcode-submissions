class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for s in operations:
            if s == "+":
                num = stack[-2] + stack[-1]
                stack.append(num)
                sum += num
            elif s == "D":
                num = stack[-1] * 2
                stack.append(num)
                sum += num
            elif s == "C":
                num = stack[-1]
                stack.pop()
                sum -= num
            else:
                stack.append(int(s))
                sum += int(s)
        return sum

        