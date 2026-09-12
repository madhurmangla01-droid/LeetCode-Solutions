class Solution:

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Iterate from the second-to-last row up to the top row
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Choose the smaller of the two adjacent values below
                triangle[row][col] += min(
                    triangle[row + 1][col], triangle[row + 1][col + 1]
                )

        # The top element now contains the minimum path sum
        return triangle[0][0]
