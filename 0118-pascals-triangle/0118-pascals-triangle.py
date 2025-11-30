class Solution:
    def generate(self, numRows: int):
        triangle = []

        for i in range(numRows):
            # start each row with 1s
            row = [1] * (i + 1)

            # fill the middle values using previous row
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)

        return triangle
