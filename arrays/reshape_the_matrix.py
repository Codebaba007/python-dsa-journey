
class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        flat = []

        for row in mat:
            for num in row:
                flat.append(num)

        res = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                res[i][j] = flat[i * c + j]

        return res