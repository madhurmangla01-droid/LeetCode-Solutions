class Solution:
    def addOperators(self, num, target):
        ans = []

        def dfs(i, exp, val, prev):
            if i == len(num):
                if val == target:
                    ans.append(exp)
                return

            for j in range(i, len(num)):
                if j > i and num[i] == "0":
                    break

                x = int(num[i:j+1])

                if i == 0:
                    dfs(j+1, str(x), x, x)
                else:
                    dfs(j+1, exp+"+"+str(x), val+x, x)
                    dfs(j+1, exp+"-"+str(x), val-x, -x)
                    dfs(j+1, exp+"*"+str(x),
                        val-prev+prev*x, prev*x)

        dfs(0, "", 0, 0)
        return ans