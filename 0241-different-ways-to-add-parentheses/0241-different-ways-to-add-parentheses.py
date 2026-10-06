class Solution:
    def diffWaysToCompute(self, expression):

        def solve(exp):
            ans = []

            for i in range(len(exp)):
                if exp[i] in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i+1:])

                    for a in left:
                        for b in right:
                            if exp[i] == "+":
                                ans.append(a + b)
                            elif exp[i] == "-":
                                ans.append(a - b)
                            else:
                                ans.append(a * b)

            return ans if ans else [int(exp)]

        return solve(expression)
        