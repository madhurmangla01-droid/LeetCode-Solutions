class Solution:
    def combinations(self, input, index, temp, ans, k):
        if index == len(input):
            if len(temp) == k:
                ans.append(temp[:])
            return
        if len(temp) == k:
            ans.append(temp[:])
            return
        temp.append(input[index])
        self.combinations(input, index + 1, temp, ans, k)
        temp.pop()
        self.combinations(input, index + 1, temp, ans, k)

    def combine(self, n, k):
        input = [i + 1 for i in range(n)]
        ans = []
        self.combinations(input, 0, [], ans, k)
        return ans