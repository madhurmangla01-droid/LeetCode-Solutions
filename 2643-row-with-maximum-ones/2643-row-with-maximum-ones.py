class Solution:
    def rowAndMaximumOnes(self, mat):
        best = 0
        ans = 0

        for i in range(len(mat)):
            count = mat[i].count(1)

            if count > best:
                best = count
                ans = i

        return [ans, best]