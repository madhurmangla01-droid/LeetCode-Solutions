


class Solution:
    def kthSmallest(self, matrix, k):
        arr = []

        for row in matrix:
            arr += row

        arr.sort()

        return arr[k - 1]